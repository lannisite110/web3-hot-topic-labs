// GameNFTDemo — 教学 Cadence 合约模板，仅测试网

access(all) contract GameNFTDemo {
    access(all) var totalSupply: UInt64

    access(all) resource NFT {
        access(all) let id: UInt64
        init(id: UInt64) { self.id = id }
    }

    init() {
        self.totalSupply = 0
    }

    access(all) fun mint(): @NFT {
        self.totalSupply = self.totalSupply + 1
        return <- create NFT(id: self.totalSupply)
    }
}
