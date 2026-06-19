// AnchorProgramDemo — 教学 Solana 程序模板，仅测试网
use anchor_lang::prelude::*;

declare_id!("11111111111111111111111111111111");

#[program]
pub mod anchor_program_demo {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        ctx.accounts.state.counter = 0;
        Ok(())
    }
}

#[account]
pub struct DemoState {
    pub counter: u64,
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = payer, space = 8 + 8)]
    pub state: Account<'info, DemoState>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}
