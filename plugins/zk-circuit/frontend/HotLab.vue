<script setup lang="ts">
import { ref, onUnmounted } from 'vue'

const param = ref('demo_circuit')
const loading = ref(false)
const error = ref('')
const result = ref<Record<string, unknown> | null>(null)
const status = ref<Record<string, unknown> | null>(null)
const report = ref<Record<string, unknown> | null>(null)
let pollTimer: ReturnType<typeof setInterval> | null = null

const PLUGIN_ID = 'edu.hot.zk-circuit'

async function runSimulate() {
  loading.value = true
  error.value = ''
  result.value = null
  status.value = null
  report.value = null
  if (pollTimer) clearInterval(pollTimer)
  try {
    const res = await fetch(`/api/v1/labs/${PLUGIN_ID}/simulate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_prompt: 'Cairo 电路编译与 Sierra 输出教学',
        params: { circuit_name: param.value },
        allowed_chain_ids: [11155111],
      }),
    })
    const data = await res.json()
    if (!res.ok) throw new Error(data.error || res.statusText)
    result.value = data
    const taskId = (data.task as Record<string, unknown> | undefined)?.id as string | undefined
    if (taskId) startPoll(taskId)
  } catch (e) {
    error.value = e instanceof Error ? e.message : String(e)
  } finally {
    loading.value = false
  }
}

function startPoll(taskId: string) {
  pollTimer = setInterval(async () => {
    try {
      const s = await fetch(`/api/v1/labs/${PLUGIN_ID}/status/${taskId}`)
      status.value = await s.json()
      const st = (status.value?.status as string) || ''
      if (st === 'completed' || st === 'failed') {
        if (pollTimer) clearInterval(pollTimer)
        const r = await fetch(`/api/v1/labs/${PLUGIN_ID}/report/${taskId}`)
        report.value = await r.json()
      }
    } catch { /* ignore poll errors */ }
  }, 1500)
}

onUnmounted(() => { if (pollTimer) clearInterval(pollTimer) })
</script>

<template>
  <section class="lab-panel">
    <header class="lab-header">
      <img src="/assets/icon.png" alt="" width="32" height="32" />
      <div>
        <h1>ZK 电路编译教学</h1>
        <p class="muted">edu.hot.zk-circuit · 测试网教学 only</p>
      </div>
    </header>
    <div class="card">
      <label>电路名称
        <input v-model="param" />
      </label>
      <button :disabled="loading" @click="runSimulate">
        { loading ? '提交中…' : '提交仿真实验' }
      </button>
      <p v-if="error" class="error">{ error }</p>
    </div>
    <pre v-if="result" class="block">simulate: { JSON.stringify(result, null, 2) }</pre>
    <pre v-if="status" class="block">status: { JSON.stringify(status, null, 2) }</pre>
    <pre v-if="report" class="block">report: { JSON.stringify(report, null, 2) }</pre>
  </section>
</template>

<style scoped>
.lab-panel { padding: 1rem; }
.lab-header { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; }
.muted { color: #64748b; font-size: 0.875rem; }
.card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; }
label { display: block; }
input { display: block; width: 100%; margin: 0.5rem 0; padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; }
button { padding: 0.5rem 1rem; background: #2563eb; color: white; border: none; border-radius: 4px; cursor: pointer; }
button:disabled { opacity: 0.6; }
.error { color: #dc2626; }
.block { margin-top: 1rem; background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; font-size: 0.8rem; }
</style>
