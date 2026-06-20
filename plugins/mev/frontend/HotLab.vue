<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabI18n } from '@/composables/useLabI18n'
import { useLabSimulate } from '../../frontend/shared/useLabSimulate'
import { parseHints, hintNumber } from '../../frontend/shared/parseHints'

const PLUGIN_ID = 'edu.hot.mev'
const { t } = useLabI18n(PLUGIN_ID)

const blockSlots = ref(12)
const builderCount = ref(3)
const slotIndex = ref(0)

const demoBuilders = computed(() =>
  Array.from({ length: builderCount.value }, (_, i) => ({
    id: `builder-${i}`,
    bid: 10 + ((i * 17 + slotIndex.value) % 80),
  })).sort((a, b) => b.bid - a.bid),
)

const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate(PLUGIN_ID)

const evaluation = computed(() => parseEvaluation(result.value?.evaluation))
const hints = computed(() => parseHints(evaluation.value?.audit_hints))

const winner = computed(() => hints.value.winning_builder ?? demoBuilders.value[0]?.id)
const winningBid = computed(() =>
  hintNumber(hints.value, 'winning_bid_gwei', demoBuilders.value[0]?.bid ?? 0),
)

function submit() {
  runSimulate('Proposer-Builder 分离算法教学仿真（非套利机器人）', {
    block_slots: blockSlots.value,
    builder_count: builderCount.value,
    slot_index: slotIndex.value,
  })
}
</script>

<template>
  <section class="lab-panel">
    <header class="lab-header">
      <img src="/assets/icon.png" alt="" width="32" height="32" />
      <div>
        <h1>{{ t('title') }}</h1>
        <p class="muted">{{ t('subtitle') }}</p>
      </div>
    </header>

    <div class="lab-grid">
      <div class="card">
        <h2>{{ t('slotParams') }}</h2>
        <label>{{ t('blockSlots') }} <input v-model.number="blockSlots" type="number" min="1" max="32" /></label>
        <label>{{ t('builderCount') }} <input v-model.number="builderCount" type="number" min="2" max="8" /></label>
        <label>{{ t('slotIndex') }} <input v-model.number="slotIndex" type="number" min="0" /></label>
        <button :disabled="loading" @click="submit">{{ loading ? t('simulating') : t('runPbs') }}</button>
        <p v-if="taskStatus" class="status">{{ t('task') }}: {{ taskStatus }}</p>
        <p v-if="error" class="error">{{ error }}</p>
      </div>

      <div class="card">
        <h2>{{ t('builderBids') }}</h2>
        <table class="bid-table">
          <thead><tr><th>Builder</th><th>{{ t('bidGwei') }}</th></tr></thead>
          <tbody>
            <tr v-for="b in demoBuilders" :key="b.id" :class="{ win: b.id === winner }">
              <td>{{ b.id }}</td>
              <td>{{ b.bid }}</td>
            </tr>
          </tbody>
        </table>
        <p class="win-line">{{ t('proposerPick') }}: <strong>{{ winner }}</strong> · {{ winningBid }} gwei</p>
        <p v-if="hints.pbs_mode" class="muted">{{ t('mode') }}: {{ hints.pbs_mode }}</p>
      </div>

      <div class="card">
        <h2>{{ t('pbsFlow') }}</h2>
        <ol class="flow">
          <li>{{ t('pbs_1') }}</li>
          <li>{{ t('pbs_2') }}</li>
          <li>{{ t('pbs_3') }}</li>
          <li>{{ t('pbs_4') }}</li>
        </ol>
        <p class="muted">Solidity: <code>MevPbsAuction.sol</code></p>
        <p class="warn">{{ t('arbWarning') }}</p>
      </div>
    </div>

    <details v-if="taskReport || result" class="raw">
      <summary>{{ t('taskReportJson') }}</summary>
      <pre>{{ JSON.stringify(taskReport ?? result, null, 2) }}</pre>
    </details>
  </section>
</template>

<style scoped>
.lab-panel { padding: 1rem; }
.lab-header { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; }
.lab-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
.card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; }
.card h2 { margin: 0 0 0.75rem; font-size: 1rem; }
label { display: block; margin-bottom: 0.5rem; font-size: 0.875rem; }
input { display: block; width: 100%; margin-top: 0.25rem; padding: 0.45rem; border: 1px solid #cbd5e1; border-radius: 4px; }
.bid-table { width: 100%; border-collapse: collapse; font-size: 0.875rem; }
.bid-table th, .bid-table td { border: 1px solid #e2e8f0; padding: 0.35rem 0.5rem; text-align: left; }
.bid-table tr.win { background: #fef9c3; font-weight: 600; }
.win-line { margin-top: 0.75rem; color: #854d0e; }
.flow { padding-left: 1.25rem; margin: 0; }
.flow li { margin-bottom: 0.35rem; }
.warn { color: #b45309; font-size: 0.875rem; margin-top: 0.5rem; }
.muted { color: #64748b; font-size: 0.875rem; }
code { font-family: monospace; font-size: 0.8rem; }
.status { color: #2563eb; font-size: 0.875rem; margin-top: 0.5rem; }
.error { color: #dc2626; }
button { margin-top: 0.5rem; padding: 0.5rem 1rem; width: 100%; background: #2563eb; color: #fff; border: none; border-radius: 4px; cursor: pointer; }
button:disabled { opacity: 0.6; }
.raw { margin-top: 1rem; }
.raw pre { background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; font-size: 0.78rem; }
</style>
