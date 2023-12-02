import random
from modules.transfer import Transfer

import modules_settings as ms
from modules.dmail import Dmail
from modules.jediswap import JediSwap
from modules.publuc_nft_mint import PublicMint
from modules.swap10k import Swap10K
from modules.unframed import Unframed
from modules.zklend import ZkLend


async def random_low_cost_modules(id, wallet, address):
    modules = [
        dmail_send, increase_allowance_unframed,
        cancel_orders_unframed, eth_transfer
    ]

    random_module = random.choice(modules)
    await random_module(id, wallet, address)

async def random_modules(id, wallet, address):
    modules = [
        dmail_send, mint_public_nft, deposit_zklend,
        increase_allowance_unframed, cancel_orders_unframed,
        swap_jediswap, swap_10k, eth_transfer
    ]

    random_module = random.choice(modules)
    await random_module(id, wallet, address)

async def dmail_send(id, wallet, address):
    dmail = Dmail(id, wallet, address)
    await dmail.send_mail()


async def mint_public_nft(id, wallet, address):
    nft_contract = ms.MintPublicNFT.nft_contract

    nft_mint = PublicMint(id, wallet, address)
    await nft_mint.mint_nft(nft_contract)


async def deposit_zklend(id, wallet, address):
    min_amount = ms.ZkLend.min_amount
    max_amount = ms.ZkLend.max_amount
    decimals = ms.ZkLend.decimals

    withdraw = ms.ZkLend.withdraw

    zklend = ZkLend(id, wallet, address)
    await zklend.deposit(min_amount, max_amount, decimals, withdraw)


async def withdraw_zklend(id, wallet, address):
    zklend = ZkLend(id, wallet, address)
    await zklend.withdraw()


async def increase_allowance_unframed(id, wallet, address):
    min_amount = ms.Unframed.IncreaseAllowance.min_amount
    max_amount = ms.Unframed.IncreaseAllowance.max_amount
    decimals = ms.Unframed.IncreaseAllowance.decimals

    unframed = Unframed(id, wallet, address)
    await unframed.increase_allowance(min_amount, max_amount, decimals)
    

async def cancel_orders_unframed(id, wallet, address):
    unframed = Unframed(id, wallet, address)
    await unframed.cancel_orders()


async def swap_jediswap(id, wallet, address):
    from_token = ms.JediSwap.from_token
    to_token = ms.JediSwap.to_token

    min_amount = ms.JediSwap.min_amount
    max_amount = ms.JediSwap.max_amount
    decimals = ms.JediSwap.decimals

    all_amount = ms.JediSwap.all_amount
    min_percent = ms.JediSwap.min_percent
    max_percent = ms.JediSwap.max_percent

    swap_reverse = ms.JediSwap.swap_reverse

    jediswap = JediSwap(id, wallet, address)
    await jediswap.swap(from_token, to_token, min_amount, max_amount, decimals, all_amount, min_percent, max_percent, swap_reverse)


async def swap_10k(id, wallet, address):
    from_token = ms.Swap10K.from_token
    to_token = ms.Swap10K.to_token

    min_amount = ms.Swap10K.min_amount
    max_amount = ms.Swap10K.max_amount
    decimals = ms.Swap10K.decimals

    all_amount = ms.Swap10K.all_amount
    min_percent = ms.Swap10K.min_percent
    max_percent = ms.Swap10K.max_percent

    swap_reverse = ms.Swap10K.swap_reverse

    swap_10k = Swap10K(id, wallet, address)
    await swap_10k.swap(from_token, to_token, min_amount, max_amount, decimals, all_amount, min_percent, max_percent, swap_reverse)


async def eth_transfer(id, wallet, address):
    min_amount = ms.Transfer.min_amount
    max_amount = ms.Transfer.max_amount
    decimals = ms.Transfer.decimals
    
    eth_transfer = Transfer(id, wallet, address)
    await eth_transfer.transfer(min_amount, max_amount, decimals)