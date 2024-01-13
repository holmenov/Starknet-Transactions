from modules.account import Account
from utils.config import STARKNET_TOKENS, ZKLEND_ABI, ZKLEND_ADDRESS
from utils.wrappers import check_gas
from utils.utils import async_sleep, send_logs


class ZkLend(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)
        
        self.contract = self.get_contract(ZKLEND_ADDRESS, ZKLEND_ABI, cairo_version=1)

    @check_gas
    async def deposit(self, min_amount: float, max_amount: float, decimals: int, withdraw: bool):
        send_logs('Deposit ETH on ZkLend.', self.account_id, self.account_address_str)
    
        amount_data = await self.get_amount('ETH', min_amount, max_amount, decimals)
        
        approve_tx = await self.approve_multicall(STARKNET_TOKENS['ETH'], ZKLEND_ADDRESS, amount_data['amount_wei'])

        deposit_tx = self.contract.functions['deposit'].prepare(STARKNET_TOKENS['ETH'], amount_data['amount_wei'])

        calls = [deposit_tx]

        if approve_tx:
            calls.insert(0, approve_tx)

        await self.execute_multicall_tx(calls=calls)

        if withdraw:
            await async_sleep(5, 20, logs=False)
            await self.withdraw()

    @check_gas
    async def withdraw(self):
        send_logs('Withdraw ETH on ZkLend.', self.account_id, self.account_address_str)

        tx = await self.contract.functions['withdraw_all'].invoke(STARKNET_TOKENS['ETH'], auto_estimate=True)

        await self.wait_until_tx_accepted(tx)