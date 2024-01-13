import random
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.account.account import Account as StarkAccount
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.contract import InvokeResult, Contract, PreparedFunctionCall
from starknet_py.net.client_models import TransactionFinalityStatus

from settings import MainSettings as SETTINGS
from utils.config import ERC20_ABI, STARKNET_TOKENS
from utils.utils import async_sleep, send_logs


class Account:
    def __init__(self, account_id: int, private_key: str, account_address: str) -> None:
        self.private_key = int(private_key, 16)
        self.account_address_str = account_address
        self.account_address = int(account_address, 16)
        
        self.account_id = account_id

        self.client = FullNodeClient(node_url=SETTINGS.STARKNET_NODE)

        self.account = StarkAccount(
            address=self.account_address,
            client=self.client,
            key_pair=KeyPair.from_private_key(key=self.private_key),
            chain=StarknetChainId.MAINNET
        )

    def get_contract(self, contract_address: int, abi: list, cairo_version: int = 0):
        contract = Contract(
            address=contract_address,
            abi=abi,
            provider=self.account,
            cairo_version=cairo_version
        )

        return contract

    async def get_contract_without_abi(self, contract_address: int):
        contract = await Contract.from_address(address=contract_address, provider=self.account)

        return contract

    async def wait_until_tx_accepted(self, tx: InvokeResult):
        tx = await tx.wait_for_acceptance()

        if tx.status == TransactionFinalityStatus.ACCEPTED_ON_L2:
            send_logs(
                f'https://starkscan.co/tx/{hex(tx.hash)} successfully!',
                self.account_id, self.account_address_str, status='success'
            )

        elif tx.status == TransactionFinalityStatus.NOT_RECEIVED:
            send_logs(
                f'https://starkscan.co/tx/{hex(tx.hash)} transaction failed!',
                self.account_id, self.account_address_str, status='error'
            )

    async def check_allowance(self, token_address: int, spender: str):
        contract = self.get_contract(token_address, ERC20_ABI)
        amount_approved = (await contract.functions['allowance'].call(self.account_address, spender)).remaining

        return amount_approved

    async def get_balance(self, contract_address: str) -> dict:
        contract = self.get_contract(contract_address, ERC20_ABI)

        symbol = (await contract.functions['symbol'].call()).symbol
        decimals = (await contract.functions['decimals'].call()).decimals
        balance_wei = (await contract.functions['balanceOf'].call(self.account_address)).balance

        balance = balance_wei / 10 ** decimals

        return {'balance_wei': balance_wei, 'balance': balance, 'symbol': symbol, 'decimals': decimals}

    async def get_amount(self, token: str, min_amount: float, max_amount: float, decimal: int) -> dict:
        balance = await self.get_balance(STARKNET_TOKENS[token])

        amount = round(random.uniform(min_amount, max_amount), decimal)
        amount_wei = int(amount * 10 ** balance['decimals'])
        balance = balance['balance_wei']

        return {'amount_wei': amount_wei, 'amount': amount, 'balance': balance}

    async def get_amount_percents(self, token: str, min_percent: int, max_percent: int) -> dict:
        balance = await self.get_balance(STARKNET_TOKENS[token])

        random_percent = random.randint(min_percent, max_percent)
        percent = 1 if random_percent == 100 else random_percent / 100

        amount_wei = int(balance['balance_wei'] * percent)
        amount = balance['balance'] * percent
        balance = balance['balance_wei']
        
        return {'amount_wei': amount_wei, 'amount': amount, 'balance': balance}

    async def approve(self, token_address: int, spender: int, amount: int):
        contract = self.get_contract(token_address, ERC20_ABI)

        allowance_amount = await self.check_allowance(token_address, spender)

        if amount > allowance_amount or amount == 0:
            send_logs('Make approve.', self.account_id, self.account_address_str)

            approve_amount = 2 ** 128 if amount > allowance_amount else 0
            tx = await contract.functions['approve'].invoke(spender, approve_amount, auto_estimate=True)

            await self.wait_until_tx_accepted(tx)

            await async_sleep(5, 10, logs=False)
    
    async def approve_multicall(self, token_address: int, spender: int, amount: int) -> PreparedFunctionCall | None:
        contract = self.get_contract(token_address, ERC20_ABI)

        allowance_amount = await self.check_allowance(token_address, spender)
        
        if amount > allowance_amount or amount == 0:
            send_logs('Make approve.', self.account_id, self.account_address_str)

            approve_amount = 2 ** 128 if amount > allowance_amount else 0
            tx_approve = contract.functions['approve'].prepare(spender, approve_amount)

            return tx_approve
    
    async def execute_multicall_tx(self, calls: list):
        tx = await self.account.execute(
            calls=calls,
            auto_estimate=True
        )

        await self.account.client.wait_for_tx(tx.transaction_hash)
        
        send_logs(
            f'https://starkscan.co/tx/{hex(tx.transaction_hash)} successfully!',
            self.account_id, self.account_address_str, status='success'
        )