# K8s Job 工具链门禁片段

Phase 3 起，热点 Lab Job 不再使用纯 `echo` 占位，而是运行 **toolchain 版本检查 + 最小编译/验证步骤**。

| 语言组 | 镜像 | 典型命令 |
|--------|------|----------|
| evm | `edu/toolchain-evm:0.1.0` | `solc --version` + 内联 Solidity 编译 |
| move | `edu/toolchain-move:0.1.0` | `aptos` / `sui` 版本检查 |
| zk | `edu/toolchain-zk:0.1.0` | `scarb --version` |
| solana | `edu/toolchain-solana:0.1.0` | `rustc` / `anchor` 版本检查 |

本地冒烟：`make k8s-job-smoke`（busybox 回退时跳过真实 toolchain）。
