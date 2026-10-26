import { readFile, writeFile } from 'node:fs/promises';
const token = process.env.APIFY_API_TOKEN;
if (!token) throw new Error('Set APIFY_API_TOKEN.');
async function api(path, body) {
  const response = await fetch('https://api.apify.com/v2' + path, {
    method: body === undefined ? 'GET' : 'POST',
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: body === undefined ? undefined : JSON.stringify(body),
    signal: AbortSignal.timeout(30000),
  });
  if (!response.ok) throw new Error(`Apify API returned HTTP ${response.status}`);
  return response.json();
}
const input = JSON.parse(await readFile(new URL('../../data/sample-input.json', import.meta.url), 'utf8'));
// Never automatically replay a start request whose acknowledgement is uncertain.
let { data: run } = await api('/acts/datascraperes~ziprecruiter-jobs-scraper/runs?build=latest&timeout=300&maxTotalChargeUsd=0.01', input);
console.log('Run ID:', run.id);
const deadline = Date.now() + 260000;
while (!['SUCCEEDED', 'FAILED', 'ABORTED', 'TIMED-OUT'].includes(run.status)) {
  if (Date.now() >= deadline) {
    await api(`/actor-runs/${run.id}/abort`, {});
    throw new Error('Watchdog requested abort; inspect the run before retrying.');
  }
  await new Promise(resolve => setTimeout(resolve, 2000));
  ({ data: run } = await api(`/actor-runs/${run.id}`));
}
const items = run.defaultDatasetId ? await api(`/datasets/${run.defaultDatasetId}/items?clean=true&limit=1000`) : [];
let summary = null;
try { summary = await api(`/key-value-stores/${run.defaultKeyValueStoreId}/records/SUMMARY`); } catch {}
await writeFile('ziprecruiter-jobs.json', JSON.stringify(items, null, 2));
const complete = run.status === 'SUCCEEDED' && ['success', 'empty'].includes(summary?.status) && summary?.outputItems === items.length;
console.log(JSON.stringify({ runId: run.id, status: run.status, complete, summaryAvailable: summary !== null, summaryStatus: summary?.status ?? null }, null, 2));
if (!complete) process.exitCode = 2;
