// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title RwaMappingDemo — 虚构 RWA 链上映射教学，非募资/发行
contract RwaMappingDemo {
    mapping(string => address) public assetRegistry;
    address public registrar;

    constructor() {
        registrar = msg.sender;
    }

    function mapAsset(string calldata assetId, address token) external {
        require(msg.sender == registrar, "not registrar");
        assetRegistry[assetId] = token;
    }
}
