import random
import secrets
from loguru import logger
from classes.Account import Account
from utils.config import ERC20_ABI, STARKNET_TOKENS
from utils.utils import check_gas


class Transfer(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)

    def generate_address(self):
        range_start = 0
        range_end = 3618502788666131213697322783095070105623107215331596699973092056135872020481
        return '0x' + format(random.randint(range_start, range_end), '064x')

    @check_gas
    async def transfer(self, min_amount: float, max_amount: float, decimals: int):
        logger.info(f'ID: {self.account_id} | {self.account_address_str} | Transfer ETH.')
        
        eth_contract = self.get_contract(STARKNET_TOKENS['ETH'], ERC20_ABI)
        
        amount_data = await self.get_amount('ETH', min_amount, max_amount, decimals)
        
        random_address = int(self.generate_address(), 16)
        
        tx = await eth_contract.functions['transfer'].invoke(
            random_address, amount_data['amount_wei'], auto_estimate=True
        )
        
        await self.wait_until_tx_accepted(tx)