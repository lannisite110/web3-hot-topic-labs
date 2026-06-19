// DePIN node demo — Anchor template, testnet only
use anchor_lang::prelude::*;

declare_id!("11111111111111111111111111111111");

#[program]
pub mod depin_node_demo {
    use super::*;
    pub fn register_node(ctx: Context<Register>, node_id: u64) -> Result<()> {
        ctx.accounts.state.node_id = node_id;
        Ok(())
    }
}

#[account]
pub struct NodeState { pub node_id: u64 }

#[derive(Accounts)]
pub struct Register<'info> {
    #[account(init, payer = payer, space = 8 + 8)]
    pub state: Account<'info, NodeState>,
    #[account(mut)] pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}
