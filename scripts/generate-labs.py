#!/usr/bin/env python3
"""Generate hot-topic lab artifacts (rules already hand-written separately)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LABS = [
    {
        "slug": "zk-modular",
        "id": "edu.hot.zk-modular",
        "name": "ZK Modular Rollup Lab",
        "title": "ZK 模块化 Rollup 教学",
        "task": "HOT_ZK_ROLLUP_SIM",
        "ns": "ns-hot-zk",
        "rule": "zk_modular",
        "contract_path": "plugins/zk-modular/contracts/ModularRollupDemo.sol",
        "language": "solidity",
        "image": "edu/toolchain-zk:0.1.0",
        "lang_group": "zk",
        "tutorial": "zk-modular-intro.md",
        "desc": "ZK 电路与 Rollup 批次提交教学仿真（测试网 mock verifier）",
        "param_key": "batch_size",
        "param_label": "Rollup 批次大小",
        "param_default": "8",
    },
    {
        "slug": "zk-circuit",
        "id": "edu.hot.zk-circuit",
        "name": "ZK Circuit Compile Lab",
        "title": "ZK 电路编译教学",
        "task": "HOT_ZK_CIRCUIT_COMPILE",
        "ns": "ns-hot-zk",
        "rule": "zk_circuit",
        "contract_path": "plugins/zk-circuit/contracts/ZkCircuit.cairo",
        "language": "cairo",
        "image": "edu/toolchain-zk:0.1.0",
        "lang_group": "zk",
        "tutorial": "zk-circuit-intro.md",
        "desc": "Cairo 电路编译与 Sierra 输出教学",
        "param_key": "circuit_name",
        "param_label": "电路名称",
        "param_default": "demo_circuit",
    },
    {
        "slug": "aa-wallet",
        "id": "edu.hot.aa-wallet",
        "name": "Account Abstraction Wallet Lab",
        "title": "账户抽象 AA 钱包教学",
        "task": "HOT_AA_WALLET_SIM",
        "ns": "ns-hot-aa",
        "rule": "aa_wallet",
        "contract_path": "plugins/aa-wallet/contracts/AAWalletDemo.sol",
        "language": "solidity",
        "image": "edu/toolchain-evm:0.1.0",
        "lang_group": "evm",
        "tutorial": "aa-wallet-intro.md",
        "desc": "ERC-4337 风格 AA 钱包测试网部署演示",
        "param_key": "owner",
        "param_label": "Owner 地址（演示）",
        "param_default": "0x0000000000000000000000000000000000000001",
    },
    {
        "slug": "aa-session",
        "id": "edu.hot.aa-session",
        "name": "AA Session Key Lab",
        "title": "会话密钥教学",
        "task": "HOT_AA_SESSION_KEY_DEMO",
        "ns": "ns-hot-aa",
        "rule": "aa_session",
        "contract_path": "plugins/aa-session/contracts/SessionKeyDemo.sol",
        "language": "solidity",
        "image": "edu/toolchain-evm:0.1.0",
        "lang_group": "evm",
        "tutorial": "aa-session-intro.md",
        "desc": "受限权限会话密钥测试网演示",
        "param_key": "session_ttl_hours",
        "param_label": "会话有效期（小时）",
        "param_default": "24",
    },
    {
        "slug": "ai-agent",
        "id": "edu.hot.ai-agent",
        "name": "AI Agent Sandbox Lab",
        "title": "AI Agent 受限沙箱",
        "task": "HOT_AI_AGENT_SANDBOX",
        "ns": "ns-hot-sim",
        "rule": "ai_agent",
        "contract_path": "plugins/ai-agent/contracts/AgentSandbox.sol",
        "language": "solidity",
        "image": "edu/toolchain-evm:0.1.0",
        "lang_group": "evm",
        "tutorial": "ai-agent-intro.md",
        "desc": "链上 Agent 权限边界教学仿真",
        "param_key": "max_actions",
        "param_label": "最大动作次数",
        "param_default": "3",
    },
    {
        "slug": "rwa-edu",
        "id": "edu.hot.rwa-edu",
        "name": "RWA Education Simulation Lab",
        "title": "RWA 链上映射教学",
        "task": "HOT_RWA_EDU_SIM",
        "ns": "ns-hot-sim",
        "rule": "rwa_edu",
        "contract_path": "plugins/rwa-edu/contracts/RwaMappingDemo.sol",
        "language": "solidity",
        "image": "edu/toolchain-evm:0.1.0",
        "lang_group": "evm",
        "tutorial": "rwa-edu-intro.md",
        "desc": "虚构资产链上映射教学（非募资/发行）",
        "param_key": "asset_id",
        "param_label": "虚构资产 ID",
        "param_default": "DEMO-RWA-001",
    },
    {
        "slug": "depin",
        "id": "edu.hot.depin",
        "name": "DePIN Node Simulation Lab",
        "title": "DePIN 节点仿真",
        "task": "HOT_DEPIN_NODE_SIM",
        "ns": "ns-hot-sim",
        "rule": "depin",
        "contract_path": "plugins/depin/contracts/DepinNode.rs",
        "language": "rust",
        "image": "edu/toolchain-solana:0.1.0",
        "lang_group": "solana",
        "tutorial": "depin-intro.md",
        "desc": "Solana Anchor DePIN 节点注册教学仿真",
        "param_key": "node_count",
        "param_label": "模拟节点数",
        "param_default": "5",
    },
    {
        "slug": "did",
        "id": "edu.hot.did",
        "name": "DID Privacy Demo Lab",
        "title": "DID 隐私演示",
        "task": "HOT_DID_PRIVACY_DEMO",
        "ns": "ns-hot-sim",
        "rule": "did",
        "contract_path": "plugins/did/contracts/DidPrivacy.move",
        "language": "move",
        "image": "edu/toolchain-move:0.1.0",
        "lang_group": "move",
        "tutorial": "did-intro.md",
        "desc": "Move 链上 DID 与选择性披露教学",
        "param_key": "did_method",
        "param_label": "DID 方法",
        "param_default": "did:demo",
    },
    {
        "slug": "mev",
        "id": "edu.hot.mev",
        "name": "MEV PBS Simulation Lab",
        "title": "MEV PBS 博弈仿真",
        "task": "HOT_MEV_PBS_SIM",
        "ns": "ns-hot-sim",
        "rule": "mev",
        "contract_path": "plugins/mev/contracts/MevPbsSim.huff",
        "language": "huff",
        "image": "edu/toolchain-evm:0.1.0",
        "lang_group": "evm",
        "tutorial": "mev-intro.md",
        "desc": "Proposer-Builder 分离算法教学仿真（非套利机器人）",
        "param_key": "block_slots",
        "param_label": "模拟区块槽位",
        "param_default": "12",
    },
    {
        "slug": "dao",
        "id": "edu.hot.dao",
        "name": "DAO Vote Simulation Lab",
        "title": "DAO 投票教学",
        "task": "HOT_DAO_VOTE_SIM",
        "ns": "ns-hot-sim",
        "rule": "dao",
        "contract_path": "plugins/dao/contracts/DaoVoteDemo.sol",
        "language": "solidity",
        "image": "edu/toolchain-evm:0.1.0",
        "lang_group": "evm",
        "tutorial": "dao-intro.md",
        "desc": "测试网 DAO 提案与投票计数教学",
        "param_key": "proposal_id",
        "param_label": "提案 ID",
        "param_default": "1",
    },
]

RULE_TEMPLATE = '''"""{name} — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("{param_key}", "{param_default}")
    return ok(
        "{contract_path}",
        "{language}",
        "{task}",
        ["{param_key}=" + str(param), "plugin_id={id}"],
    )
'''

MANIFEST_TEMPLATE = """apiVersion: edu.web3/v1
kind: PluginPackage
metadata:
  id: {id}
  name: {name}
  version: 0.1.0
  repo: web3-hot-topic-labs
  compliance_tier: hot_topic

spec:
  coreVersion: ">=0.1.0 <0.2.0"
  taskTypes:
    - {task}
  namespaces:
    - {ns}
  allowedChainIds:
    - 11155111
  frontend:
    routePrefix: /labs/{id}
    entry: plugins/{slug}/frontend/plugin.ts
  rules:
    entry: plugins.rules.{rule}:evaluate
  contracts:
    - path: {contract_path}
      language: {language}
  k8s:
    jobTemplate: k8s/overlays/{ns}/{slug}-job.yaml
  docs:
    - docs/tutorials/{tutorial}
"""

K8S_TEMPLATE = """apiVersion: batch/v1
kind: Job
metadata:
  name: {slug}-sim
  labels:
    edu.web3/plugin-id: {id}
    edu.web3/lang-group: {lang_group}
    edu.web3/compliance: testnet-only
spec:
  backoffLimit: 1
  template:
    metadata:
      labels:
        edu.web3/plugin-id: {id}
    spec:
      restartPolicy: Never
      containers:
        - name: runner
          image: {image}
          env:
            - name: CHAIN_ID
              value: "11155111"
            - name: TASK_TYPE
              value: "{task}"
            - name: EDU_LANG_GROUP
              value: "{lang_group}"
            - name: RPC_URL
              valueFrom:
                configMapKeyRef:
                  name: testnet-rpc-sepolia
                  key: rpc_url
          command:
            - sh
            - -c
            - |
              echo "[testnet] plugin={id} task=${{TASK_TYPE}} chain=${{CHAIN_ID}}"
              echo "Simulation completed (educational only)"
"""

TUTORIAL_TEMPLATE = """# {title}

> **插件**: `{id}` · **TaskType**: `{task}` · **Namespace**: `{ns}`

## 原理

{desc}

## 操作步骤

1. 主库启动后端：`make run-rule-engine` / `run-scheduler` / `run-gateway`
2. 注册插件：`make register-plugins PLUGINS_DIR=..`
3. 打开 `/labs/{id}`，填写参数并提交仿真实验
4. 轮询任务状态并查看报告 JSON

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网部署演示 | 主网上线 |
| 教学仿真与算法演示 | 生产级 Rollup / 真实交易策略 |
| 虚构数据 | 资产发行/募资/套利机器人 |
"""

PLUGIN_TS = """export const plugin = {{
  id: '{id}',
  title: '{name}',
  routePrefix: '/labs/{id}',
  routes: [{{ path: '', component: () => import('./HotLab.vue') }}],
  apiBase: '/api/v1/labs/{id}',
}}

export default plugin
"""

VUE_TEMPLATE = """<script setup lang="ts">
import {{ ref, onUnmounted }} from 'vue'

const param = ref('{param_default}')
const loading = ref(false)
const error = ref('')
const result = ref<Record<string, unknown> | null>(null)
const status = ref<Record<string, unknown> | null>(null)
const report = ref<Record<string, unknown> | null>(null)
let pollTimer: ReturnType<typeof setInterval> | null = null

const PLUGIN_ID = '{id}'

async function runSimulate() {{
  loading.value = true
  error.value = ''
  result.value = null
  status.value = null
  report.value = null
  if (pollTimer) clearInterval(pollTimer)
  try {{
    const res = await fetch(`/api/v1/labs/${{PLUGIN_ID}}/simulate`, {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{
        user_prompt: '{desc}',
        params: {{ {param_key}: param.value }},
        allowed_chain_ids: [11155111],
      }}),
    }})
    const data = await res.json()
    if (!res.ok) throw new Error(data.error || res.statusText)
    result.value = data
    const taskId = (data.task as Record<string, unknown> | undefined)?.id as string | undefined
    if (taskId) startPoll(taskId)
  }} catch (e) {{
    error.value = e instanceof Error ? e.message : String(e)
  }} finally {{
    loading.value = false
  }}
}}

function startPoll(taskId: string) {{
  pollTimer = setInterval(async () => {{
    try {{
      const s = await fetch(`/api/v1/labs/${{PLUGIN_ID}}/status/${{taskId}}`)
      status.value = await s.json()
      const st = (status.value?.status as string) || ''
      if (st === 'completed' || st === 'failed') {{
        if (pollTimer) clearInterval(pollTimer)
        const r = await fetch(`/api/v1/labs/${{PLUGIN_ID}}/report/${{taskId}}`)
        report.value = await r.json()
      }}
    }} catch {{ /* ignore poll errors */ }}
  }}, 1500)
}}

onUnmounted(() => {{ if (pollTimer) clearInterval(pollTimer) }})
</script>

<template>
  <section class="lab-panel">
    <header class="lab-header">
      <img src="/assets/icon.png" alt="" width="32" height="32" />
      <div>
        <h1>{title}</h1>
        <p class="muted">{id} · 测试网教学 only</p>
      </div>
    </header>
    <div class="card">
      <label>{param_label}
        <input v-model="param" />
      </label>
      <button :disabled="loading" @click="runSimulate">
        {{ loading ? '提交中…' : '提交仿真实验' }}
      </button>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
    <pre v-if="result" class="block">simulate: {{ JSON.stringify(result, null, 2) }}</pre>
    <pre v-if="status" class="block">status: {{ JSON.stringify(status, null, 2) }}</pre>
    <pre v-if="report" class="block">report: {{ JSON.stringify(report, null, 2) }}</pre>
  </section>
</template>

<style scoped>
.lab-panel {{ padding: 1rem; }}
.lab-header {{ display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; }}
.muted {{ color: #64748b; font-size: 0.875rem; }}
.card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; }}
label {{ display: block; }}
input {{ display: block; width: 100%; margin: 0.5rem 0; padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; }}
button {{ padding: 0.5rem 1rem; background: #2563eb; color: white; border: none; border-radius: 4px; cursor: pointer; }}
button:disabled {{ opacity: 0.6; }}
.error {{ color: #dc2626; }}
.block {{ margin-top: 1rem; background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; font-size: 0.8rem; }}
</style>
"""


def write_contract(lab: dict) -> None:
    path = ROOT / lab["contract_path"]
    path.parent.mkdir(parents=True, exist_ok=True)
    lang = lab["language"]
    slug = lab["slug"]
    if path.exists():
        return
    if lang == "solidity":
        content = f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title {lab['name']} — 教学模板，仅测试网
contract Demo {{
    uint256 public value;

    function setValue(uint256 v) external {{
        value = v;
    }}
}}
"""
    elif lang == "cairo":
        content = f"""// {lab['name']} — 教学 Cairo 模板，仅测试网
#[starknet::contract]
mod Demo {{
    #[storage]
    struct Storage {{ value: u64 }}

    #[external(v0)]
    fn set_value(ref self: ContractState, v: u64) {{
        self.value.write(v);
    }}
}}
"""
    elif lang == "rust":
        content = """// DePIN node demo — Anchor template, testnet only
use anchor_lang::prelude::*;

declare_id!("11111111111111111111111111111111");

#[program]
pub mod depin_node_demo {
    use super::*;
    pub fn register_node(ctx: Context<Register>, node_id: u64) -> Result<()> {
        ctx.accounts.state.node_id = node_id;
        Ok(())
    }
}

#[account]
pub struct NodeState { pub node_id: u64 }

#[derive(Accounts)]
pub struct Register<'info> {
    #[account(init, payer = payer, space = 8 + 8)]
    pub state: Account<'info, NodeState>,
    #[account(mut)] pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}
"""
    elif lang == "move":
        content = """// DID privacy demo — Move template, testnet only
module demo::did_privacy {
    struct DidRecord has key { method: vector<u8> }
    public entry fun register(account: &signer, method: vector<u8>) {
        move_to(account, DidRecord { method });
    }
}
"""
    elif lang == "huff":
        content = """/// MEV PBS demo — Huff template, testnet only
#define constant COUNTER = 0x00
#define macro INCREMENT() = takes (0) returns (0) {
    [COUNTER] sload
    1 add
    [COUNTER] sstore
    stop
}
"""
    else:
        content = f"// {slug} placeholder\n"
    path.write_text(content, encoding="utf-8")


def main() -> None:
    for lab in LABS:
        slug = lab["slug"]
        rule_path = ROOT / "plugins" / "rules" / f"{lab['rule']}.py"
        rule_path.write_text(RULE_TEMPLATE.format(**lab), encoding="utf-8")

        manifest_path = ROOT / "plugins" / slug / "plugin.manifest.yaml"
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(MANIFEST_TEMPLATE.format(**lab), encoding="utf-8")

        k8s_path = ROOT / "k8s" / "overlays" / lab["ns"] / f"{slug}-job.yaml"
        k8s_path.parent.mkdir(parents=True, exist_ok=True)
        k8s_path.write_text(K8S_TEMPLATE.format(**lab), encoding="utf-8")

        tut_path = ROOT / "docs" / "tutorials" / lab["tutorial"]
        tut_path.parent.mkdir(parents=True, exist_ok=True)
        tut_path.write_text(TUTORIAL_TEMPLATE.format(**lab), encoding="utf-8")

        fe_dir = ROOT / "plugins" / slug / "frontend"
        fe_dir.mkdir(parents=True, exist_ok=True)
        (fe_dir / "plugin.ts").write_text(PLUGIN_TS.format(**lab), encoding="utf-8")
        (fe_dir / "HotLab.vue").write_text(VUE_TEMPLATE.format(**lab), encoding="utf-8")

        write_contract(lab)
        print(f"generated {slug}")


if __name__ == "__main__":
    main()
