// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title DaoVoteDemo — DAO 投票计数教学，仅测试网
contract DaoVoteDemo {
    mapping(uint256 => uint256) public yesVotes;
    mapping(uint256 => uint256) public noVotes;
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    function vote(uint256 proposalId, bool support) external {
        require(!hasVoted[msg.sender][proposalId], "already voted");
        hasVoted[msg.sender][proposalId] = true;
        if (support) yesVotes[proposalId] += 1;
        else noVotes[proposalId] += 1;
    }
}
