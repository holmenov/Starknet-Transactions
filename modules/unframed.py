import random
from loguru import logger
from classes.Account import Account
from utils.config import ERC20_ABI, STARKNET_TOKENS, UNFRAMED_ABI, UNFRAMED_ADDRESS
from utils.utils import check_gas


class Unframed(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)

    @check_gas
    async def increase_allowance(self, min_amount: float, max_amount: float, decimals: int):
        logger.info(f'ID: {self.account_id} | {self.account_address_str} | Increase allowance for Unframed.')
        
        eth_contract = self.get_contract(STARKNET_TOKENS['ETH'], ERC20_ABI)
        
        amount_data = await self.get_amount('ETH', min_amount, max_amount, decimals)
        
        tx = await eth_contract.functions['increaseAllowance'].invoke(
            UNFRAMED_ADDRESS, amount_data['amount_wei'], auto_estimate=True
        )
        
        await self.wait_until_tx_accepted(tx)

    @check_gas
    async def cancel_orders(self):
        logger.info(f'ID: {self.account_id} | {self.account_address_str} | Cancel orders Unframed.')
        
        eth_contract = self.get_contract(UNFRAMED_ADDRESS, UNFRAMED_ABI, cairo_version=1)
        
        order = random.randint(
            667804429319483499453779488538666086956476410672792319212669697953101601261,
            2632968113723259089783301048934457955080170763850563370503425240771722598032
        )
        
        tx = await eth_contract.functions['cancel_orders'].invoke(
            [order], auto_estimate=True
        )
        
        await self.wait_until_tx_accepted(tx)