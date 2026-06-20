// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title MevPbsAuction — Proposer-Builder Separation 教学 mock，仅测试网
/// @notice 演示 Builder 对 slot 出价、Proposer 选最高 bid；非 MEV 套利机器人
contract MevPbsAuction {
    struct BuilderBid {
        address builder;
        uint256 value;
    }

    mapping(uint256 => BuilderBid[]) public slotBids;
    mapping(uint256 => address) public selectedBuilder;

    event BidSubmitted(uint256 indexed slot, address indexed builder, uint256 value);
    event BuilderSelected(uint256 indexed slot, address indexed builder, uint256 winningBid);

    function submitBid(uint256 slot) external payable {
        slotBids[slot].push(BuilderBid(msg.sender, msg.value));
        emit BidSubmitted(slot, msg.sender, msg.value);
    }

    function selectWinningBuilder(uint256 slot) external returns (address winner, uint256 maxVal) {
        BuilderBid[] storage bids = slotBids[slot];
        require(bids.length > 0, "no bids");
        winner = bids[0].builder;
        maxVal = bids[0].value;
        for (uint256 i = 1; i < bids.length; i++) {
            if (bids[i].value > maxVal) {
                maxVal = bids[i].value;
                winner = bids[i].builder;
            }
        }
        selectedBuilder[slot] = winner;
        emit BuilderSelected(slot, winner, maxVal);
    }
}
