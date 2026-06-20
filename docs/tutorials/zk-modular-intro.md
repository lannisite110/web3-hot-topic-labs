# ZK 模块化 Rollup 教学 · 分步实验

> **插件**: `edu.hot.zk-modular` · **TaskType**: `HOT_ZK_ROLLUP_SIM` · **Namespace**: `ns-hot-zk`  
> **合约**: `plugins/zk-modular/contracts/ModularRollupDemo.sol`  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 2 步 · 入口来自 [language-advisor-intro.md](language-advisor-intro.md)

---

## 学习目标

- 理解 L2 批次收集 → Mock 证明 → 提交 → L1 锚定流水线  
- 阅读 `mock_batch_root` / `tx_count` audit_hints  
- 区分教学 mock verifier 与生产 Rollup  

---

## 分步实验

### 步骤 1：从 language-advisor 跳转（推荐）

1. 打开 `/labs/edu.hot.language-advisor`  
2. 选场景 **ZK Rollup** → 获取推荐 → **打开专题 Lab →**  

### 步骤 2：Rollup UI

1. 设置批次大小 (1–64)  
2. 点击 **提交批次仿真实验**  
3. 观察流水线四步高亮与批次列表  

### 步骤 3：curl

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.zk-modular/simulate \
  -H 'Content-Type: application/json' \
  -d '{"user_prompt":"zk rollup batch","params":{"batch_size":8},"allowed_chain_ids":[11155111]}' \
  | jq '.evaluation.audit_hints'
```

**期望**：含 `mock_batch_root=0x...`、`verifier=mock-sepolia`。

---

## K8s

`zk-modular-job.yaml` 运行 `scarb --version` toolchain gate。

---

## 相关链接

- 下一篇：[zk-circuit-intro.md](zk-circuit-intro.md)  

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| Mock ZK / 测试网 Rollup 演示 | 生产级 Rollup 部署方案 |
| 教学批次与 root | 主网资金桥接 |

> **合规脚注**: testnet-only · mock verifier only
