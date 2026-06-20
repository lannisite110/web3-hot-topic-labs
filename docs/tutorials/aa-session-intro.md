# 会话密钥教学 · 分步实验

> **插件**: `edu.hot.aa-session` · **TaskType**: `HOT_AA_SESSION_KEY_DEMO` · **Namespace**: `ns-hot-aa`  
> **合约**: `plugins/aa-session/contracts/SessionKeyDemo.sol`  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 3 步

---

## 学习目标

- 理解 AA 钱包下的 **受限权限会话密钥** 与 TTL  
- 对比 [aa-wallet-intro.md](aa-wallet-intro.md) 中 Owner 全权限 UserOp  

---

## 分步实验

### 步骤 1

打开 `/labs/edu.hot.aa-session`，设置 **会话有效期（小时）**（默认 24），提交仿真。

### 步骤 2：curl

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.aa-session/simulate \
  -H 'Content-Type: application/json' \
  -d '{"user_prompt":"session key demo","params":{"session_ttl_hours":48},"allowed_chain_ids":[11155111]}' \
  | jq '.evaluation'
```

### 步骤 3：思考

- 会话密钥应能限制 callData 范围（合约模板为教学简化）  
- 过期后应拒绝 execute（可在合约 `SessionKeyDemo.sol` 中阅读）  

---

## 相关

- 上一篇：[aa-wallet-intro.md](aa-wallet-intro.md)  
- 下一篇：[dao-intro.md](dao-intro.md)  

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网 session key 演示 | 主网无限授权密钥 |

> **合规脚注**: testnet-only · 虚构 session 数据
