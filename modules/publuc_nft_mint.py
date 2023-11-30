from loguru import logger

from classes.Account import Account
from utils.config import NFT_ABI
from utils.utils import check_gas


class PublicMint(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)

    @check_gas
    async def mint_nft(self, contract_address: str):
        logger.info(f'ID: {self.account_id} | {self.account_address} | Mint public NFT.')

        contract = self.get_contract(contract_address, NFT_ABI)

        tx = await contract.functions["publicMint"].invoke(
            self.account_address, auto_estimate=True
        )

        await self.wait_until_tx_accepted(tx)
