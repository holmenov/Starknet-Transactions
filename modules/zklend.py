from loguru import logger
from classes.Account import Account
from utils.config import STARKNET_TOKENS, ZKLEND_ABI, ZKLEND_ADDRESS
from utils.utils import check_gas, sleep


class ZkLend(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)
        
        self.contract = self.get_contract(ZKLEND_ADDRESS, ZKLEND_ABI)

    @check_gas
    async def deposit(self, min_amount: float, max_amount: float, decimals: int, withdraw: bool):
        logger.info(f'ID: {self.account_id} | {self.account_address} | Deposit ETH on ZkLend.')
    
        amount_data = await self.get_amount('ETH', min_amount, max_amount, decimals)
        
        approve_tx = await self.approve_multicall(STARKNET_TOKENS['ETH'], ZKLEND_ADDRESS, amount_data['amount_wei'])

        deposit_tx = self.contract.functions['deposit'].prepare(STARKNET_TOKENS['ETH'], amount_data['amount_wei'])

        calls = [deposit_tx]

        if approve_tx:
            calls.insert(0, approve_tx)

        await self.execute_multicall_tx(calls=calls)

        if withdraw:
            await sleep(5, 20)
            await self.withdraw()

    @check_gas
    async def withdraw(self):
        logger.info(f'ID: {self.account_id} | {self.account_address} | Withdraw ETH on ZkLend.')

        tx = await self.contract.functions['withdraw_all'].invoke(STARKNET_TOKENS['ETH'], auto_estimate=True)

        await self.wait_until_tx_accepted(tx)