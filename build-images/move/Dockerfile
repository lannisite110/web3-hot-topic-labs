# Move 工具链镜像：aptos + sui CLI
# 教学用途，测试网 only
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Aptos CLI (pinned installer)
RUN curl -fsSL "https://aptos.dev/scripts/install_cli.sh" | sh
ENV PATH="/root/.local/bin:${PATH}"

# Sui CLI (pinned release binary)
RUN curl -fsSL https://github.com/MystenLabs/sui/releases/download/testnet-v1.21.1/sui-ubuntu-x86_64.tgz \
    | tar -xz -C /usr/local/bin sui

WORKDIR /workspace
ENV EDU_LANG_GROUP=move
ENTRYPOINT ["bash", "-c", "echo '==> Move toolchain ready (testnet-only)' && exec \"$@\"", "--"]
