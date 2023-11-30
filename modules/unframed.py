from loguru import logger
from classes.Account import Account
from utils.config import ERC20_ABI, STARKNET_TOKENS, UNFRAMED_ADDRESS
from utils.utils import check_gas


class Unframed(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)

    @check_gas
    async def increase_allowance(self, min_amount: float, max_amount: float, decimals: int):
        logger.info(f'ID: {self.account_id} | {self.account_address} | Increase allowance for Unframed.')
        
        eth_contract = self.get_contract(STARKNET_TOKENS['ETH'], ERC20_ABI)
        
        amount_data = await self.get_amount('ETH', min_amount, max_amount, decimals)
        
        tx = await eth_contract.functions['increaseAllowance'].invoke(
            UNFRAMED_ADDRESS, amount_data['amount_wei'], auto_estimate=True
        )
        
        await self.wait_until_tx_accepted(tx)