from loguru import logger

from classes.Account import Account
from utils.config import DMAIL_ABI, DMAIL_ADDRESS
from utils.utils import check_gas, get_random_string


class Dmail(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)
    
    @check_gas
    async def send_mail(self):
        logger.info(f'ID: {self.account_id} | {self.account_address_str} | Send mail via Dmail.')
        
        contract = self.get_contract(DMAIL_ADDRESS, DMAIL_ABI)
        
        random_email = (get_random_string() + '@gmail.com').encode()
        random_theme = (get_random_string()).encode()

        tx = await contract.functions['transaction'].invoke(
            random_email.hex(), random_theme.hex(), auto_estimate=True
        )

        await self.wait_until_tx_accepted(tx)