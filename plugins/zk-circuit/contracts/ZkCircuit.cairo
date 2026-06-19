// ZkCircuitDemo — 教学 Cairo 电路模板，仅测试网
#[starknet::contract]
mod ZkCircuit {
    #[storage]
    struct Storage {
        sum: u64,
    }

    #[external(v0)]
    fn accumulate(ref self: ContractState, delta: u64) {
        self.sum.write(self.sum.read() + delta);
    }

    #[external(v0)]
    fn get_sum(self: @ContractState) -> u64 {
        self.sum.read()
    }
}
