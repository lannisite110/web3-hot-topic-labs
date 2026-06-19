# @version ^0.4.0
# VaultDemo — 教学金库模板，仅测试网

owner: public(address)

@deploy
def __init__():
    self.owner = msg.sender

@external
@payable
def deposit():
    pass

@external
def withdraw(amount: uint256):
    assert msg.sender == self.owner, "not owner"
    send(msg.sender, amount)
