<p align="center">
  <img src="assets/icon.png" alt="Web3 Education Platform" width="128"/>
</p>

# Web3 Hot Topic Labs

Web3 前沿热点**教学插件包**（子库1）。

## 核心能力

1. **多语言合约执行层** — 7 语言组独立镜像/Namespace（见 `docs/multi-language-toolchains.md`）
2. **智能语言择优** — `edu.hot.language-advisor` 按业务自动推荐最优合约语言
3. **10 个热点 Lab** — ZK / AA / MEV / DAO 等（共 **11** 插件含择优入口）

依赖 [web3-edu-platform-core](../web3-edu-platform-core) ≥ v0.1.0。

## 插件清单（11）

| plugin_id | Lab |
|-----------|-----|
| `edu.hot.language-advisor` | 智能语言择优 |
| `edu.hot.zk-modular` | ZK 模块化 Rollup |
| `edu.hot.zk-circuit` | ZK 电路编译 |
| `edu.hot.aa-wallet` | 账户抽象 AA |
| `edu.hot.aa-session` | 会话密钥 |
| `edu.hot.ai-agent` | AI Agent 沙箱 |
| `edu.hot.rwa-edu` | RWA 教学仿真 |
| `edu.hot.depin` | DePIN 节点仿真 |
| `edu.hot.did` | DID 隐私 |
| `edu.hot.mev` | MEV PBS 仿真 |
| `edu.hot.dao` | DAO 投票 |

## 联合调试

```bash
cd ../web3-edu-platform-core
make register-plugins PLUGINS_DIR=..
bash ../web3-hot-topic-labs/scripts/joint-debug-smoke.sh
```

手动启动：`make run-rule-engine` / `run-scheduler` / `run-gateway`，前端访问 `/labs/edu.hot.*`。

## 智能择优速查

| 场景 | 语言 |
|------|------|
| 普通 DeFi | Solidity |
| 金库/高安全 | Vyper |
| Gas 优化/撮合内核 | Huff |
| Solana 高性能 | Rust (Anchor) |
| NFT/资产安全 | Move |
| ZK-Rollup | Cairo |
| 比特币二层 | Clarity |
| 链游/IP NFT | Cadence |
| 合规支付 | TEAL |

## 开发

见 [TASK.md](TASK.md) · 批量生成脚本 `scripts/generate-labs.py`

## 合规

测试网 + 仿真 only · [COMPLIANCE_MASTER.md](../COMPLIANCE_MASTER.md)

License: PolyForm Noncommercial 1.0.0
