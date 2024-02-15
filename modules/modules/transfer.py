import random

from modules.account import Account
from utils.config import ERC20_ABI, STARKNET_TOKENS
from utils.wrappers import check_gas
from utils.utils import send_logs, read_file_to_list


class Transfer(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)

    def generate_address(self):
        range_start = 0
        range_end = 3618502788666131213697322783095070105623107215331596699973092056135872020481
        return '0x' + format(random.randint(range_start, range_end), '064x')

    @check_gas
    async def transfer(self, min_amount: float, max_amount: float, decimals: int):
        send_logs('Transfer ETH.', self.account_id, self.account_address_str)
        
        eth_contract = self.get_contract(STARKNET_TOKENS['ETH'], ERC20_ABI)
        
        amount_data = await self.get_amount('ETH', min_amount, max_amount, decimals)
        
        random_address = int(self.generate_address(), 16)
        
        tx = await eth_contract.functions['transfer'].invoke(
            random_address, amount_data['amount_wei'], auto_estimate=True
        )
        
        await self.wait_until_tx_accepted(tx)
    
    @check_gas
    async def transfer_eth_to_cex(self, min_percent: float, max_percent: float):
        send_logs('Transfer ETH to CEX.', self.account_id, self.account_address_str)
        
        eth_contract = self.get_contract(STARKNET_TOKENS['ETH'], ERC20_ABI)
        
        amount_data = await self.get_amount_percents('ETH', min_percent, max_percent)
        
        address_receive = read_file_to_list('wallets_cex.txt')[self.account_id-1]
        
        print(address_receive, self.account_address_str)
        
        tx = await eth_contract.functions['transfer'].invoke(
            address_receive, amount_data['amount_wei'], auto_estimate=True
        )

        await self.wait_until_tx_accepted(tx)