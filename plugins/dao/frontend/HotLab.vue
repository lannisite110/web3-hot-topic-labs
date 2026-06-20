<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabSimulate } from '../../frontend/shared/useLabSimulate'
import { parseHints, hintNumber } from '../../frontend/shared/parseHints'

const proposalId = ref('1')
const proposalTitle = ref('增加 Sepolia 测试网教学预算')
const quorum = ref(100)
const yesVotes = ref(42)
const noVotes = ref(18)
const voterName = ref('0xDemoVoter…001')

const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate('edu.hot.dao')

const evaluation = computed(() => parseEvaluation(result.value?.evaluation))
const hints = computed(() => parseHints(evaluation.value?.audit_hints))

const displayYes = computed(() => hintNumber(hints.value, 'yes_votes', yesVotes.value))
const displayNo = computed(() => hintNumber(hints.value, 'no_votes', noVotes.value))
const displayQuorum = computed(() => hintNumber(hints.value, 'quorum_target', quorum.value))
const status = computed(() => hints.value.proposal_status ?? 'draft')
const turnout = computed(() => hints.value.turnout_pct ?? '0')

const totalVotes = computed(() => displayYes.value + displayNo.value)
const yesPct = computed(() =>
  totalVotes.value ? Math.round((100 * displayYes.value) / totalVotes.value) : 0,
)

function castVote(support: boolean) {
  if (support) yesVotes.value += 1
  else noVotes.value += 1
}

function submit() {
  runSimulate('测试网 DAO 提案与投票计数教学', {
    proposal_id: proposalId.value,
    proposal_title: proposalTitle.value,
    quorum: quorum.value,
    yes_votes: yesVotes.value,
    no_votes: noVotes.value,
    last_voter: voterName.value,
  })
}
</script>

<template>
  <section class="lab-panel">
    <header class="lab-header">
      <img src="/assets/icon.png" alt="" width="32" height="32" />
      <div>
        <h1>DAO 投票教学</h1>
        <p class="muted">虚构治理 · Sepolia · 一人一票演示</p>
      </div>
    </header>

    <div class="lab-grid">
      <div class="card">
        <h2>提案</h2>
        <label>提案 ID <input v-model="proposalId" /></label>
        <label>标题 <input v-model="proposalTitle" /></label>
        <label>法定 quorum <input v-model.number="quorum" type="number" min="1" /></label>
        <label>演示投票人 <input v-model="voterName" /></label>
        <div class="vote-actions">
          <button type="button" class="yes" @click="castVote(true)">投 YES +1</button>
          <button type="button" class="no" @click="castVote(false)">投 NO +1</button>
        </div>
        <button class="submit" :disabled="loading" @click="submit">
          {{ loading ? '上链仿真中…' : '提交投票快照到平台' }}
        </button>
        <p v-if="taskStatus" class="status">任务: {{ taskStatus }}</p>
        <p v-if="error" class="error">{{ error }}</p>
      </div>

      <div class="card">
        <h2>计票板</h2>
        <p class="status-badge" :class="status">{{ status }}</p>
        <div class="tally">
          <div class="bar yes-bar" :style="{ width: yesPct + '%' }" />
        </div>
        <div class="counts">
          <span class="yes">YES {{ displayYes }}</span>
          <span class="no">NO {{ displayNo }}</span>
        </div>
        <p class="muted">出席率 {{ turnout }}% · quorum 目标 {{ displayQuorum }}</p>
        <p class="muted">本地计数 YES {{ yesVotes }} / NO {{ noVotes }}（提交前可调整）</p>
      </div>

      <div class="card">
        <h2>治理流程</h2>
        <ol class="gov-flow">
          <li :class="{ done: proposalTitle.length > 0 }">起草提案</li>
          <li :class="{ done: totalVotes > 0 }">成员投票</li>
          <li :class="{ done: status === 'passed' || status === 'rejected' }">计票公示</li>
          <li :class="{ done: taskStatus === 'completed' }">链上仿真记录</li>
        </ol>
        <p class="muted">合约模板: <code>DaoVoteDemo.sol</code></p>
      </div>
    </div>

    <details v-if="taskReport || result" class="raw">
      <summary>任务报告 JSON</summary>
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
.vote-actions { display: flex; gap: 0.5rem; margin: 0.75rem 0; }
.vote-actions button { flex: 1; padding: 0.45rem; border: none; border-radius: 4px; cursor: pointer; color: #fff; }
.yes { background: #16a34a; }
.no { background: #dc2626; }
.submit { width: 100%; padding: 0.5rem; background: #2563eb; color: #fff; border: none; border-radius: 4px; cursor: pointer; }
.submit:disabled { opacity: 0.6; }
.status-badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 999px; font-size: 0.8rem; text-transform: uppercase; font-weight: 600; }
.status-badge.draft { background: #e2e8f0; }
.status-badge.active { background: #dbeafe; color: #1d4ed8; }
.status-badge.passed { background: #dcfce7; color: #166534; }
.status-badge.rejected { background: #fee2e2; color: #991b1b; }
.tally { height: 10px; background: #fee2e2; border-radius: 999px; overflow: hidden; margin: 0.75rem 0; }
.yes-bar { height: 100%; background: #22c55e; transition: width 0.3s; }
.counts { display: flex; justify-content: space-between; font-weight: 600; }
.counts .yes { color: #15803d; }
.counts .no { color: #b91c1c; }
.gov-flow { padding-left: 1.25rem; }
.gov-flow li { margin-bottom: 0.4rem; color: #94a3b8; }
.gov-flow li.done { color: #15803d; font-weight: 500; }
.muted { color: #64748b; font-size: 0.875rem; }
code { font-family: monospace; font-size: 0.8rem; }
.status { color: #2563eb; font-size: 0.875rem; margin-top: 0.5rem; }
.error { color: #dc2626; }
.raw { margin-top: 1rem; }
.raw pre { background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; font-size: 0.78rem; }
</style>
