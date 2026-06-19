# Solana 工具链镜像：rust + anchor CLI
# 教学用途，测试网 only
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git build-essential pkg-config libssl-dev ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Rust toolchain (pinned channel)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain 1.79.0
ENV PATH="/root/.cargo/bin:${PATH}"

# Anchor CLI (pinned)
RUN cargo install --locked --version 0.30.1 anchor-cli

WORKDIR /workspace
ENV EDU_LANG_GROUP=solana
ENTRYPOINT ["bash", "-c", "echo '==> Solana toolchain ready (testnet-only)' && exec \"$@\"", "--"]
