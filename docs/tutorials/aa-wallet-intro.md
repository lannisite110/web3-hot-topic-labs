# 账户抽象 AA 钱包 · 4337 流程实验

> **插件**: `edu.hot.aa-wallet` · **TaskType**: `HOT_AA_WALLET_SIM` · **Namespace**: `ns-hot-aa`  
> **合约**: `plugins/aa-wallet/contracts/AAWalletDemo.sol`  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 3 步

---

## 学习目标

- 走通 ERC-4337 风格五步：Build → Sign → Bundle → Validate → Execute  
- 理解 UserOp hash 与 EntryPoint 校验（教学 mock）  
- 对比 Owner 地址与 Smart Account 角色  

---

## 分步实验

### 步骤 1：打开 Lab

`http://127.0.0.1:5173/labs/edu.hot.aa-wallet`

### 步骤 2：流程 UI

1. 填写 Owner 地址与 callData  
2. 在下拉框选择模拟执行到哪一步（如 `validate` / `execute`）  
3. 点击流程图某一步可切换当前步骤  
4. **提交 AA 流程仿真**  
5. 查看 UserOp Hash 与 `aa_flow_completed` hints  

### 步骤 3：curl

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.aa-wallet/simulate \
  -H 'Content-Type: application/json' \
  -d '{
    "user_prompt": "AA wallet demo",
    "params": {
      "owner": "0x0000000000000000000000000000000000000001",
      "aa_flow_step": "execute",
      "call_data": "0xdeadbeef"
    },
    "allowed_chain_ids": [11155111]
  }' | jq '.evaluation.audit_hints'
```

---

## 相关链接

- 下一篇：[aa-session-intro.md](aa-session-intro.md)  
- 主库 DEV：[DEV.md](https://github.com/lannisite110/web3-edu-platform-core/blob/main/docs/DEV.md)  

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网 AA / UserOp 教学 | 主网 Bundler 攻击 / 资金盗取 |
| Mock EntryPoint | 生产 Paymaster 滥用 |

> **合规脚注**: testnet-only · mock 4337 flow
