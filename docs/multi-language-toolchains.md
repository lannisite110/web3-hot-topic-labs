# 多语言合约执行层

> **归属**: `web3-hot-topic-labs`（工具链镜像 + 择优规则）  
> **调度**: 主库 `control-plane-go/container-manager` 按语言组拉起对应 Job  
> **原则**: 每种语言 **独立镜像、独立 Namespace、独立编译环境**，互不冲突

---

## 1. 语言组与工具链

| 语言组 | 原生工具 | 镜像目录 | K8s Namespace | 典型输出 |
|--------|----------|----------|----------------|----------|
| **EVM** | solc, vyper, huff, foundry | `build-images/evm/` | `ns-evm` | `.bin`, `.abi`, gas report |
| **Solana** | rust, anchor | `build-images/solana/` | `ns-solana` | `.so program |
| **Move** | aptos CLI, sui CLI | `build-images/move/` | `ns-move` | Move bytecode |
| **ZK** | cairo, starknet-foundry | `build-images/zk/` | `ns-hot-zk` | Sierra, CASM |
| **BTC L2** | clarity | `build-images/btc/` | `ns-lang-btc` | Clarity AST/部署包 |
| **Flow** | cadence | `build-images/flow/` | `ns-lang-flow` | Cadence CDC |
| **Algorand** | pyteal, teal | `build-images/algorand/` | `ns-lang-algorand` | TEAL 模板 |

---

## 2. 隔离模型

```
Podman 本地构建（开发者）
    ↓
Docker 打 tag → 私有仓库 edu/{lang-group}:{version}
    ↓
K8s Job（仅挂载该语言组工具链，无共享 /usr/bin）
    ↓
NetworkPolicy：禁止跨 Namespace 访问其他语言编译器 Pod
```

- 每个 Job 标签：`edu.web3/lang-group=evm|solana|move|...`
- 资源配额：每 Namespace 独立 CPU/内存上限（主库 Operator 创建）

---

## 3. 与热点 Lab 的关系

| 场景 | 使用语言组 |
|------|------------|
| ZK Rollup Lab | ZK 组（cairo） |
| AA Wallet Lab | EVM 组（solidity/foundry） |
| DePIN Lab | Solana 组（anchor） |
| 通用择优入口 | `plugins/language-advisor` 自动路由 |

热点 Lab **不自带编译器**；提交任务时带 `language_group`，调度器选镜像。

---

## 4. 合规

- 所有编译/部署 Job 强制 `CHAIN_ID` 为测试网白名单
- 镜像内 **预装** 工具链，运行时 **禁止** curl 安装额外二进制（Supply Chain 安全）

---

## 5. Agent-1 交付清单

- [x] 7 个 `build-images/*/Dockerfile`（含 EVM vyper/huff）
- [x] `build-images/manifest.yaml` 语言组 → 镜像 tag 映射
- [x] `k8s/overlays/ns-evm/` + `ns-lang-{btc,flow,algorand}/` Job 模板
- [x] `plugins/language-advisor/` 智能择优插件（manifest + 9 模板 + rules）
- [x] `scripts/joint-debug-smoke.sh` 联合调试冒烟
