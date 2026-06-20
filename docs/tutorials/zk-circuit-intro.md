# ZK 电路编译教学 · 分步实验

> **插件**: `edu.hot.zk-circuit` · **TaskType**: `HOT_ZK_CIRCUIT_COMPILE` · **Namespace**: `ns-hot-zk`  
> **合约**: `plugins/zk-circuit/contracts/ZkCircuit.cairo`  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 2 步

---

## 学习目标

- 理解 Cairo 电路与 Sierra 编译概念（教学级）  
- 提交 `circuit_name` 参数并查看规则评估  
- 关联 ZK toolchain Job（scarb）  

---

## 分步实验

### 步骤 1

打开 `http://127.0.0.1:5173/labs/edu.hot.zk-circuit`，填写电路名称（如 `demo_circuit`），提交仿真。

### 步骤 2：curl

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.zk-circuit/simulate \
  -H 'Content-Type: application/json' \
  -d '{"user_prompt":"cairo circuit compile","params":{"circuit_name":"demo_circuit"},"allowed_chain_ids":[11155111]}' \
  | jq '.evaluation'
```

### 步骤 3：自检

- [ ] `recommended_language` 为 cairo  
- [ ] 任务 completed；可选查看 Job 报告  

---

## 相关

- 上一篇：[zk-modular-intro.md](zk-modular-intro.md)  
- 工具链：[multi-language-toolchains.md](../multi-language-toolchains.md)  

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网 Cairo 编译教学 | 主网 ZK 电路部署 |
| 沙箱 scarb gate | 生产证明系统 |

> **合规脚注**: testnet-only · sandbox compile only
