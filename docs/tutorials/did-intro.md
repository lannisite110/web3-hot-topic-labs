# DID 隐私演示 · 选择性披露实验

> **插件**: `edu.hot.did` · **TaskType**: `HOT_DID_PRIVACY_DEMO` · **Namespace**: `ns-hot-sim`  
> **合约**: `plugins/did/contracts/DidPrivacy.move` · **Job**: `k8s/overlays/ns-hot-sim/did-job.yaml`  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 5 步

---

## 学习目标

- 理解 DID 注册与 **选择性披露**（只 reveal 必要 claim）  
- 对比 `revealed_field` 与 `withheld_hash`  
- 验证 `proof_valid` 规则输出  

---

## 前置条件

主库已启动；Move toolchain Job 需 K8s + `edu/toolchain-move` 镜像（可选）。

---

## 背景原理

`DidPrivacy.move` 存储 `disclosed_claim`（可展示）与 `withheld_claim_hash`（仅 hash，不泄露原文）。验证方请求特定 claim 时，链上/规则层只返回允许披露的部分。

---

## 分步实验

### 步骤 1：打开 Lab

`http://127.0.0.1:5173/labs/edu.hot.did`

### 步骤 2：UI 配置披露

1. 填写 DID 方法（如 `did:demo:edu`）  
2. 选择 **披露级别**（标准 / 最小 / 不披露）  
3. 选择要验证的 claim（email / age / country）  
4. 点击 **提交披露证明仿真**  
5. 查看「证明: 有效 ✓ / 无效 ✗」  

### 步骤 3：curl 验证

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.did/simulate \
  -H 'Content-Type: application/json' \
  -d '{
    "user_prompt": "DID selective disclosure",
    "params": {
      "did_method": "did:demo:edu",
      "disclosure_level": "email",
      "requested_claim": "email"
    },
    "allowed_chain_ids": [11155111]
  }' | jq '.evaluation'
```

**期望**：`proof_valid` 相关 hint 为 `true`；`revealed_field` 含演示邮箱。

### 步骤 4：对比实验

将 `disclosure_level` 设为 `none`，再次提交 — 应看到 `proof_valid=false`。

---

## 自检清单

- [ ] 理解 withheld 字段不以明文返回  
- [ ] Move Job gate：`aptos` / `sui` 版本检查（cluster）  

---

## 相关链接

- [depin-intro.md](depin-intro.md) · [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md)  

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| 虚构 DID / 演示 claim | 真实公民 PII / 护照数据 |
| 测试网 Move 教学 | 主网身份绑定 |

> **合规脚注**: testnet-only · 虚构身份数据 only
