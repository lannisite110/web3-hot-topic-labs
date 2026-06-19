# EVM 工具链镜像：solc + vyper + huff + foundry
# 教学用途，测试网 only — 运行时禁止 curl 安装额外二进制
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git build-essential ca-certificates python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

# solc (pinned)
RUN curl -fsSL https://github.com/ethereum/solidity/releases/download/v0.8.26/solc-static-linux \
    -o /usr/local/bin/solc && chmod +x /usr/local/bin/solc

# vyper (pinned via pip)
RUN pip3 install --no-cache-dir vyper==0.4.0

# foundry (forge/cast/anvil)
RUN curl -L https://foundry.paradigm.xyz | bash
ENV PATH="/root/.foundry/bin:${PATH}"
RUN foundryup

# huff compiler (pinned release)
RUN curl -fsSL https://github.com/huff-language/huff-rs/releases/download/v0.3.2/huff-linux-x86_64 \
    -o /usr/local/bin/huff && chmod +x /usr/local/bin/huff

WORKDIR /workspace
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
