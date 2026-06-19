// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title ModularRollupDemo — ZK Rollup 批次提交教学 mock，仅测试网
/// @notice 使用 mock verifier，禁止用于生产 Rollup
contract ModularRollupDemo {
    address public admin;
    uint256 public batchCount;
    mapping(uint256 => bytes32) public batchRoots;

    event BatchSubmitted(uint256 indexed batchId, bytes32 root);

    constructor() {
        admin = msg.sender;
    }

    /// @dev 教学用 mock：任意 root 均可提交，无真实 ZK 验证
    function submitBatch(bytes32 root) external {
        require(msg.sender == admin, "not admin");
        batchCount += 1;
        batchRoots[batchCount] = root;
        emit BatchSubmitted(batchCount, root);
    }

    function latestRoot() external view returns (bytes32) {
        return batchRoots[batchCount];
    }
}
