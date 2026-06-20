# Changelog

## v0.4.0 — 2026-06-20

热点 Lab Phase 0–4 完整交付。

### Phase 0 — 基础
- `useLabSimulate` composable · 修复 `generate-labs.py` Vue `{{ }}` bug
- 10 个 `HotLab.vue` 统一任务状态 + 规则评估卡片

### Phase 1 — language-advisor 入口
- 结构化推荐 UI · `suggested_lab` 跳转 · `HOT_MULTI_LANG_COMPILE`
- `advisorTypes.ts` · 规则/API 扩展字段

### Phase 2 — 领域 UI
- `zk-modular` / `dao` / `aa-wallet` 三列 grid 与领域交互

### Phase 3 — 合约 / Job 对齐
- `MevPbsAuction.sol` · `DidPrivacy.move` 选择性披露
- 10 个 K8s Job toolchain gate（替代 echo 占位）

### Phase 4 — 教程与联调
- [HOT_TOPIC_LEARNING_PATH.md](docs/HOT_TOPIC_LEARNING_PATH.md)
- [tutorials/README.md](docs/tutorials/README.md) · 11 篇分步教程扩写
- 主库 [LEARNING_PATH 阶段 3A](https://github.com/lannisite110/web3-edu-platform-core/blob/main/docs/LEARNING_PATH.md)

---

## v0.3.0 — 2026-06-19

- `coreVersion: ">=0.6.0 <2.0.0"` 对齐主库 v1.0.0
- `docs/LEARNING_PATH.md` + `docs/QUICK_DEPLOY.md`
- toolchain manifest `0.3.0`

## v0.2.0

- 11 插件首发 · 多语言 toolchain
