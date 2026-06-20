# 智能合约语言择优 — 操作教程

> **插件**: `edu.hot.language-advisor` · **Phase 1–4 入口 Lab**  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 1 步 · 教程索引：[tutorials/README.md](README.md)

## 学习目标

- 按业务场景匹配 `language-choice-rules.yaml` 规则  
- 使用结构化 UI 查看语言 / toolchain / suggested_lab  
- 可选触发 `HOT_MULTI_LANG_COMPILE` Job  

## 原理

平台根据用户描述的业务场景，匹配 `plugins/rules/language-choice-rules.yaml` 中的关键词规则，推荐最优合约语言与工具链组（EVM / Solana / Move / ZK 等）。

## 分步实验

### 步骤 1：环境

```bash
cd ~/web3home/web3-edu-platform-core
make register-plugins PLUGINS_DIR=..
make run-rule-engine & make run-scheduler & make run-gateway &
cd frontend-web && npm run dev
```

### 步骤 2：UI

1. 打开 `/labs/edu.hot.language-advisor`  
2. 点击场景 chip（如「ZK Rollup」「Solana 高性能」）  
3. **获取语言推荐** → 查看推荐卡片  
4. **打开专题 Lab →** 跳转到建议插件  
5. （可选）**提交多语言编译 Job**  

### 步骤 3：curl — 语言推荐

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.language-advisor/simulate \
  -H 'Content-Type: application/json' \
  -d '{"user_prompt":"zk rollup cairo","params":{},"allowed_chain_ids":[11155111]}' | jq .
```

期望：`evaluation.suggested_lab=edu.hot.zk-modular`，`recommended_language=cairo`。

### 步骤 4：curl — 编译 Job

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.language-advisor/simulate \
  -H 'Content-Type: application/json' \
  -d '{"user_prompt":"compile cairo","params":{"language":"cairo"},"task_type":"HOT_MULTI_LANG_COMPILE","allowed_chain_ids":[11155111]}' | jq .
```

### 步骤 5：自检

- [ ] 9 个场景 chip 均可切换  
- [ ] suggested_lab 链接可打开对应 Lab  
- [ ] 主库 [LEARNING_PATH 阶段 3A](https://github.com/lannisite110/web3-edu-platform-core/blob/main/docs/LEARNING_PATH.md) 已阅读  

## 相关文档

- [multi-language-toolchains.md](../multi-language-toolchains.md)  
- [language-choice-rules.yaml](../../plugins/rules/language-choice-rules.yaml)  

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网部署演示 | 主网上线 |
| 语言/工具链教学推荐 | 真实交易策略 |
| 多语言编译 Job 仿真 | 生产级 Rollup 部署 |

---

> **合规脚注**: testnet-only · 虚构数据 only
