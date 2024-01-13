import time

from modules.account import Account
from settings import MainSettings as SETTINGS
from utils.config import SWAP10K_ABI, SWAP10K_ADDRESS, STARKNET_TOKENS
from utils.wrappers import check_gas
from utils.utils import send_logs


class Swap10K(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)
        
        self.contract = self.get_contract(SWAP10K_ADDRESS, SWAP10K_ABI)

    async def get_amount_out(self, from_token: str, to_token: str, amount_wei: int) -> int:
        response_data = await self.contract.functions['getAmountsOut'].call(
            amount_wei, [STARKNET_TOKENS[from_token], STARKNET_TOKENS[to_token]]
        )
        
        amount_out = response_data.amounts[1]
        
        amount_out = int(amount_out - (amount_out * SETTINGS.SLIPPAGE // 100))
        
        return amount_out

    @check_gas
    async def swap(
        self,
        from_token: str,
        to_token: str,
        min_amount: float,
        max_amount: float,
        decimals: int,
        all_amount: bool,
        min_percent: int,
        max_percent: int,
        swap_reverse: bool
    ):  
        send_logs(f'{from_token} -> {to_token} | Swap on 10KSwap.', self.account_id, self.account_address_str)
        
        if all_amount:
            amount_data = await self.get_amount_percents(from_token, min_percent, max_percent)
        else:
            amount_data = await self.get_amount(from_token, min_amount, max_amount, decimals)

        amount_out = await self.get_amount_out(from_token, to_token, amount_data['amount_wei'])

        approve_tx = await self.approve_multicall(STARKNET_TOKENS[from_token], SWAP10K_ADDRESS, amount_data['amount_wei'])
        
        swap_tx = self.contract.functions['swapExactTokensForTokens'].prepare(
            amount_data['amount_wei'],
            amount_out,
            [STARKNET_TOKENS[from_token], STARKNET_TOKENS[to_token]],
            self.account_address,
            int(time.time() + 10000),
        )
        
        calls = [swap_tx]
        
        if approve_tx:
            calls.insert(0, approve_tx)

        await self.execute_multicall_tx(calls=calls)
        
        if swap_reverse:
            await self.swap(to_token, from_token, min_amount, max_amount, decimals, True, min_percent, max_percent, False)