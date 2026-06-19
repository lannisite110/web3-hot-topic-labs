// ZkRollupDemo — 教学 Cairo 合约模板，仅测试网
#[starknet::contract]
mod ZkRollupDemo {
    #[storage]
    struct Storage {
        batch_count: u64,
    }

    #[abi(embed_v0)]
    impl DemoImpl of super::IDemo<ContractState> {
        fn increment(ref self: ContractState) {
            self.batch_count.write(self.batch_count.read() + 1);
        }

        fn get_count(self: @ContractState) -> u64 {
            self.batch_count.read()
        }
    }

    #[starknet::interface]
    trait IDemo<TContractState> {
        fn increment(ref self: TContractState);
        fn get_count(self: @TContractState) -> u64;
    }
}
