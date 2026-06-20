# Web3 热点 Lab · 分阶段路线图

> **仓库**: `web3-hot-topic-labs` · 依赖主库 ≥ v1.0.0

---

## Phase 0 — 基础修复与统一 composable ✅

**目标**: 热点 10 个 Lab 面板能正确渲染、共用 simulate 逻辑，不再复制粘贴。

| 项 | 内容 |
|----|------|
| 共享 composable | `plugins/frontend/shared/useLabSimulate.ts` |
| Vue 模板 bug | `generate-labs.py` 改用 `$placeholder$`，避免 `.format()` 吃掉 `{{ }}` |
| 10 个 HotLab | 统一：任务状态、规则评估卡片、JSON 报告 |
| 再生命令 | `python3 scripts/generate-labs.py --vue-only`（不覆盖 manifest） |

**验收**:

```bash
cd ../web3-edu-platform-core
make register-plugins PLUGINS_DIR=..
cd frontend-web && npm run build
# 浏览器打开任意 edu.hot.* Lab，按钮应显示「提交仿真实验」而非字面量 { loading ? ... }
```

---

## Phase 1 — language-advisor 入口深化 ✅

**目标**: 语言择优成为热点专题的「总入口」，结构化展示 + 跳转 + 编译 Job。

| 项 | 内容 |
|----|------|
| 结构化 UI | 9 场景 chip、`LanguageAdvisorLab.vue` 推荐卡片（语言 / 工具链 / namespace / tools） |
| 规则输出 | `language_choice.py` 增加 `suggested_lab`；rule-engine 返回 `toolchain_group` / `reason` 等 |
| 跳转 | 「打开专题 Lab →」经 registry 路由到 `suggested_lab` |
| 编译 Job | 按钮触发 `task_type: HOT_MULTI_LANG_COMPILE`（网关支持可选 `task_type`） |
| 共享类型 | `plugins/frontend/shared/advisorTypes.ts` |

**验收**: 选「ZK Rollup」→ 推荐 Cairo → 跳转 `edu.hot.zk-modular` → 可选提交编译 Job。

---

## Phase 2 — 代表 Lab 领域 UI ✅

**目标**: `zk-modular` / `dao` / `aa-wallet` 对齐溯源 Lab 的多卡片体验。

| Lab | 领域 UI | 规则增强 |
|-----|---------|----------|
| `edu.hot.zk-modular` | Rollup 流水线、批次列表、mock root | `batch_size` → tx_count / mock_batch_root |
| `edu.hot.dao` | 计票板、YES/NO 按钮、治理流程 | `yes_votes` / `quorum` → proposal_status |
| `edu.hot.aa-wallet` | 4337 五步流程、UserOp hash | `aa_flow_step` → completed steps |

共享：`plugins/frontend/shared/parseHints.ts`

**验收**: 三 Lab 均为三列 grid；DAO 可本地点票再提交；AA 可选流程步骤。

---

## Phase 3 — 规则 + 合约 + Job 与主题一致 ✅

| 项 | 内容 |
|----|------|
| **MEV** | `MevPbsAuction.sol` PBS 拍卖合约；规则输出 winning_builder/bid；Job 内联 solc 编译 |
| **DID** | `DidPrivacy.move` 选择性披露；规则 `revealed`/`withheld`/`proof_valid`；Move toolchain gate |
| **DAO Job** | solc 编译 `DaoVoteDemo` 片段（Phase 2 UI 已有计票） |
| **全部 10 热点 Job** | 从 `echo` 升级为 toolchain 版本 + 编译/验证步骤 |
| **文档** | `k8s/snippets/README.md` |

**验收**: `mev`/`did` 三列 grid UI；`grep -r "Simulation completed" k8s/overlays` 无结果。

---

## Phase 4 — 教程与联调文档 ✅

| 项 | 内容 |
|----|------|
| 教程扩写 | 11 篇 `docs/tutorials/*-intro.md`：学习目标、分步 UI/curl、自检、合规 |
| 教程索引 | [tutorials/README.md](tutorials/README.md) |
| 热点总路线 | [HOT_TOPIC_LEARNING_PATH.md](HOT_TOPIC_LEARNING_PATH.md) |
| 主库交叉链接 | `web3-edu-platform-core/docs/LEARNING_PATH.md` 阶段 **3A** |

**验收**:

```bash
cd ../web3-edu-platform-core
make tutorial-audit PLUGINS_DIR=..
```

---

## 阶段完成

Phase 0–4 全部完成。后续可按需深化单 Lab 或发版打 tag。
