import random

from modules.dmail import Dmail
from modules.jediswap import JediSwap
from modules.publuc_nft_mint import PublicMint
from modules.swap10k import Swap10K
from modules.unframed import Unframed
from modules.zklend import ZkLend


async def random_launch(id, wallet, address):
    # Write in the list the name of functions you want to use in randomization
    modules = [
        dmail_send, increase_allowance_unframed, cancel_orders_unframed
    ]

    random_module = random.choice(modules)
    await random_module(id, wallet, address)


async def dmail_send(id, wallet, address):
    dmail = Dmail(id, wallet, address)
    await dmail.send_mail()


async def mint_public_nft(id, wallet, address):
    nft_contract = 0x00b719f69b00a008a797dc48585449730aa1c09901fdbac1bc94b3bdc287cf76  # Quantum Leap

    nft_mint = PublicMint(id, wallet, address)
    await nft_mint.mint_nft(nft_contract)


async def deposit_zklend(id, wallet, address):
    min_amount = 0.0005
    max_amount = 0.0009
    decimals = 50

    withdraw = True

    zklend = ZkLend(id, wallet, address)
    await zklend.deposit(min_amount, max_amount, decimals, withdraw)


async def increase_allowance_unframed(id, wallet, address):
    min_amount = 0.00001
    max_amount = 0.00009
    decimals = 6

    unframed = Unframed(id, wallet, address)
    await unframed.increase_allowance(min_amount, max_amount, decimals)
    

async def cancel_orders_unframed(id, wallet, address):
    unframed = Unframed(id, wallet, address)
    await unframed.cancel_orders()


async def swap_jediswap(id, wallet, address):
    from_token = 'ETH'
    to_token = 'USDC'

    min_amount = 0.0005
    max_amount = 0.0009
    decimals = 5

    all_amount = False
    min_percent = 10
    max_percent = 20

    swap_reverse = True

    jediswap = JediSwap(id, wallet, address)
    await jediswap.swap(from_token, to_token, min_amount, max_amount, decimals, all_amount, min_percent, max_percent, swap_reverse)

async def swap_10k(id, wallet, address):
    from_token = 'ETH'
    to_token = 'USDC'

    min_amount = 0.0005
    max_amount = 0.0009
    decimals = 5

    all_amount = False
    min_percent = 10
    max_percent = 20

    swap_reverse = True

    swap_10k = Swap10K(id, wallet, address)
    await swap_10k.swap(from_token, to_token, min_amount, max_amount, decimals, all_amount, min_percent, max_percent, swap_reverse)