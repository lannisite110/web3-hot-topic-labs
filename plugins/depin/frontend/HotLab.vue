<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabSimulate } from '../../frontend/shared/useLabSimulate'

const param = ref('5')
const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate('edu.hot.depin')

const evaluation = computed(() => parseEvaluation(result.value?.evaluation))

function submit() {
  runSimulate('Solana Anchor DePIN 节点注册教学仿真', { node_count: param.value })
}
</script>

<template>
  <section class="lab-panel">
    <header class="lab-header">
      <img src="/assets/icon.png" alt="" width="32" height="32" />
      <div>
        <h1>DePIN 节点仿真</h1>
        <p class="muted">edu.hot.depin · 测试网教学 only</p>
      </div>
    </header>
    <div class="card">
      <label>模拟节点数
        <input v-model="param" />
      </label>
      <button :disabled="loading" @click="submit">
        {{ loading ? '提交中…' : '提交仿真实验' }}
      </button>
      <p v-if="taskStatus" class="status">任务状态: {{ taskStatus }}</p>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
    <div v-if="evaluation" class="eval-card">
      <h2>规则评估</h2>
      <p v-if="evaluation.compliance_passed !== false" class="ok">合规检查通过</p>
      <p v-if="evaluation.recommended_template">
        推荐模板: <code>{{ evaluation.recommended_template }}</code>
      </p>
      <p v-if="evaluation.recommended_language">
        推荐语言: <code>{{ evaluation.recommended_language }}</code>
      </p>
      <ul v-if="evaluation.audit_hints?.length">
        <li v-for="(hint, i) in evaluation.audit_hints" :key="i">{{ hint }}</li>
      </ul>
    </div>
    <pre v-if="taskReport" class="block">{{ JSON.stringify(taskReport, null, 2) }}</pre>
    <pre v-else-if="result" class="block">{{ JSON.stringify(result, null, 2) }}</pre>
  </section>
</template>

<style scoped>
.lab-panel { padding: 1rem; }
.lab-header { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; }
.muted { color: #64748b; font-size: 0.875rem; }
.card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; margin-bottom: 1rem; }
.eval-card { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 1rem; margin-bottom: 1rem; }
.eval-card h2 { margin: 0 0 0.5rem; font-size: 1rem; }
.eval-card .ok { color: #15803d; margin: 0 0 0.5rem; }
label { display: block; }
input { display: block; width: 100%; margin: 0.5rem 0; padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; }
button { padding: 0.5rem 1rem; background: #2563eb; color: white; border: none; border-radius: 4px; cursor: pointer; }
button:disabled { opacity: 0.6; }
.status { color: #0369a1; font-size: 0.875rem; margin-top: 0.5rem; }
.error { color: #dc2626; }
.block { margin-top: 1rem; background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; font-size: 0.8rem; }
code { font-size: 0.85em; }
</style>
