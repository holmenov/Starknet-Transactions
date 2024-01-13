from modules.account import Account
from utils.config import NFT_ABI
from utils.wrappers import check_gas
from utils.utils import send_logs


class PublicMint(Account):
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        super().__init__(account_id, private_key, account_address)

    @check_gas
    async def mint_nft(self, contract_address: str):
        send_logs('Mint public NFT.', self.account_id, self.account_address_str)

        contract = self.get_contract(contract_address, NFT_ABI)

        tx = await contract.functions["publicMint"].invoke(
            self.account_address, auto_estimate=True
        )

        await self.wait_until_tx_accepted(tx)
