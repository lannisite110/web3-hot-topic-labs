// DID privacy demo — Move template, testnet only
module demo::did_privacy {
    struct DidRecord has key { method: vector<u8> }
    public entry fun register(account: &signer, method: vector<u8>) {
        move_to(account, DidRecord { method });
    }
}
