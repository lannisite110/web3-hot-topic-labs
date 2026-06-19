# 任务书 · web3-hot-topic-labs

> **图标**: `assets/icon.png`（全平台统一）  
> **仓库**: `web3-hot-topic-labs`  
> **依赖主库**: `web3-edu-platform-core` ≥ v0.3.0  
> **compliance_tier**: `hot_topic`  
> **禁止**: 修改主库；主网；真实交易策略；生产级 Rollup 部署方案

---

## 1. 你的目标

### 1A. 多语言合约执行层（7 语言组，环境完全隔离）

见 [docs/multi-language-toolchains.md](docs/multi-language-toolchains.md)。

| 语言组 | 工具 | 镜像 | Namespace |
|--------|------|------|-----------|
| EVM | solc, vyper, huff, foundry | `build-images/evm/` | ns-evm |
| Solana | rust, anchor | `build-images/solana/` | ns-solana |
| Move | aptos, sui CLI | `build-images/move/` | ns-move |
| ZK | cairo, starknet-foundry | `build-images/zk/` | ns-hot-zk |
| BTC L2 | clarity | `build-images/btc/` | ns-lang-btc |
| Flow | cadence | `build-images/flow/` | ns-lang-flow |
| Algorand | pyteal, teal | `build-images/algorand/` | ns-lang-algorand |

### 1B. 智能择优核心（language-advisor 插件）

| 业务场景 | 推荐语言 |
|----------|----------|
| 普通 DeFi、通用合约 | Solidity |
| 资金池、金库、极高安全 | Vyper |
| 极致 Gas、高频撮合内核 | Huff |
| Solana 高 TPS | Rust (Anchor) |
| NFT、资产安全、防重放 | Move |
| ZK-Rollup、零知识 | Cairo |
| 比特币二层 | Clarity |
| 链游、IP NFT | Cadence |
| 极简合规支付 | TEAL |

规则配置：`plugins/rules/language-choice-rules.yaml`  
插件 ID：`edu.hot.language-advisor`

### 1C. Web3 热点 Lab（10 个）

| # | Lab | plugin_id | TaskType | Namespace |
|---|-----|-----------|----------|-----------|
| 1 | 模块化 Rollup / ZK | `edu.hot.zk-modular` | `HOT_ZK_ROLLUP_SIM` | ns-hot-zk |
| 2 | ZK 电路编译 | `edu.hot.zk-circuit` | `HOT_ZK_CIRCUIT_COMPILE` | ns-hot-zk |
| 3 | 账户抽象 AA | `edu.hot.aa-wallet` | `HOT_AA_WALLET_SIM` | ns-hot-aa |
| 4 | 会话密钥 | `edu.hot.aa-session` | `HOT_AA_SESSION_KEY_DEMO` | ns-hot-aa |
| 5 | AI Agent 沙箱 | `edu.hot.ai-agent` | `HOT_AI_AGENT_SANDBOX` | ns-hot-sim |
| 6 | RWA 教学仿真 | `edu.hot.rwa-edu` | `HOT_RWA_EDU_SIM` | ns-hot-sim |
| 7 | DePIN 节点仿真 | `edu.hot.depin` | `HOT_DEPIN_NODE_SIM` | ns-hot-sim |
| 8 | DID 隐私 | `edu.hot.did` | `HOT_DID_PRIVACY_DEMO` | ns-hot-sim |
| 9 | MEV PBS 仿真 | `edu.hot.mev` | `HOT_MEV_PBS_SIM` | ns-hot-sim |
| 10 | DAO 投票 | `edu.hot.dao` | `HOT_DAO_VOTE_SIM` | ns-hot-sim |

（MEV/DAO 等共用 `ns-hot-sim`，通过 NetworkPolicy 逻辑隔离。）

---

## 2. 目录结构（必须遵守）

```
web3-hot-topic-labs/
├── assets/icon.png                  # 全平台统一图标
├── build-images/                    # 7 语言组独立 Dockerfile
│   ├── manifest.yaml
│   ├── evm/ solana/ move/ zk/ btc/ flow/ algorand/
├── docs/multi-language-toolchains.md
├── plugins/
│   ├── language-advisor/            # 智能择优入口
│   ├── rules/                       # language_choice.py + yaml
│   ├── zk-modular/
│   │   ├── plugin.manifest.yaml
│   │   ├── contracts/ModularRollupDemo.sol
│   │   ├── rules/zk_modular.py      # evaluate()
│   │   └── frontend/ZkModularLab.vue + plugin.ts
│   ├── aa-wallet/
│   │   └── ...
│   └── ... (共 10 个)
├── k8s/overlays/
│   ├── ns-hot-zk/
│   ├── ns-hot-aa/
│   └── ns-hot-sim/
└── docs/tutorials/                  # 每个 Lab 至少 1 篇
```

---

## 3. 每个 Lab 最低交付

- [ ] `plugin.manifest.yaml` 通过 `make validate-plugin`
- [ ] `plugins/rules/*.py` 实现 `evaluate(RuleInput) -> RuleOutput`
- [ ] 至少 1 个教学合约模板（Solidity/Rust/Cairo 择一）
- [ ] Vue 面板：参数表单 + 提交 + 状态轮询 + 报告展示
- [ ] K8s Job 模板：`CHAIN_ID=11155111`，RPC 引用主库 ConfigMap
- [ ] 教程 MD：原理说明 + 操作步骤 + **合规边界**（测试网 only）

---

## 4. 合规用语（面板与文档）

| 允许 | 禁止 |
|------|------|
| 「测试网部署演示」 | 「主网上线」 |
| 「ZK 电路教学」 | 「生产级 Rollup」 |
| 「MEV 博弈仿真算法」 | 「套利机器人」 |
| 「RWA 链上映射教学」 | 「资产发行/募资」 |
| 「Agent 受限权限沙箱」 | 「高频自动交易」 |

---

## 5. Python rules 模板

```python
# plugins/zk-modular/rules/zk_modular.py
from dataclasses import dataclass
from typing import Any

@dataclass
class RuleInput:
    user_prompt: str
    params: dict[str, Any]
    allowed_chain_ids: list

@dataclass
class RuleOutput:
    recommended_template: str
    recommended_language: str
    audit_hints: list[str]
    compliance_passed: bool
    rejection_reason: str | None = None

def evaluate(inp: RuleInput) -> RuleOutput:
    if inp.params.get("target_network") == "mainnet":
        return RuleOutput("", "", [], False, "mainnet forbidden")
    return RuleOutput(
        recommended_template="plugins/zk-modular/contracts/ModularRollupDemo.sol",
        recommended_language="solidity",
        audit_hints=["Use testnet-only verifier mock"],
        compliance_passed=True,
    )
```

manifest 中 `rules.entry` 写：`plugins.rules.zk_modular:evaluate`（主库集成时会把子库加入 PYTHONPATH）。

---

## 6. 验收命令

```bash
cd ../web3-edu-platform-core
for m in ../web3-hot-topic-labs/plugins/*/plugin.manifest.yaml; do
  make validate-plugin MANIFEST="$m"
done
make compliance-check  # 在主库对子库路径扫描：bash ci/compliance/compliance-check.sh ../web3-hot-topic-labs
```

---

## 7. 完成报告格式

```markdown
## 交付报告
- 插件数量: 10
- manifest 列表: ...
- 未实现项: ...
- 主库集成说明: 运行 register-plugins 后 registry 条目
```

---

## v0.2.0 发布

- **版本**: `0.2.0`（见 `VERSION`）
- **主库对齐**: `spec.coreVersion: ">=0.3.0 <0.4.0"`，依赖 core **≥ v0.3.0**
- **变更**: 11 插件 manifest semver 升级；`build-images/manifest.yaml` 版本同步；教程合规脚注齐套
- **验收**: `make validate-plugin` × 11 · `make register-plugins` · `joint-debug-smoke.sh`
