import random
import string
import sys
import time
from typing import Callable
from loguru import logger
from web3 import Web3
import asyncio

from settings import MAX_GAS, SLEEP_AFTER_WORK_FROM, SLEEP_AFTER_WORK_TO
from utils.config import ADDRESSES, WALLETS


def get_wallets():
    if len(WALLETS) != len(ADDRESSES):
        logger.error('The number of wallets and addresses do not match')
        sys.exit()

    elif len(WALLETS) < 1:
        logger.error('It seems you forgot to enter the wallets')
        sys.exit()

    data = [{'id': id, 'wallet': wallet, 'address': address}
            for id, (wallet, address) in enumerate(zip(WALLETS, ADDRESSES), start=1)]

    return data


def check_gas(func):
    async def wrapper(*args, **kwargs):
        w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
        gas_price_gwei = round(w3.from_wei(w3.eth.gas_price, 'gwei'), 0)

        if gas_price_gwei > MAX_GAS:
            logger.warning(f'The gas value is higher than the value set in MAX_GAS. Expecting a decrease in the GAS price. Current gas: {gas_price_gwei} gwei.')

            while gas_price_gwei > MAX_GAS:
                await asyncio.sleep(1)

        await func(*args, **kwargs)

    return wrapper


def _async_run_module(module: Callable, id: int, wallet: str, address: str):
    try:
        asyncio.run(run_module(module, id, wallet, address))
    except Exception as e:
        logger.error(f'ID: {id} | {wallet} | An error occurred: {e}.')


async def run_module(module: Callable, id: int, wallet: str, address: str):
    await module(id, wallet, address)
    await sleep(SLEEP_AFTER_WORK_FROM, SLEEP_AFTER_WORK_TO)


async def sleep(sleep_from: int, sleep_to: int):
    delay = random.randint(sleep_from, sleep_to)
    logger.info(f'💤 Sleep {delay} s.')

    for _ in range(delay):
        await asyncio.sleep(1)


def get_random_string() -> str:
    letters = string.ascii_lowercase + string.digits
    length = random.randint(2, 4)
    random_str = ''.join(random.choice(letters) for _ in range(length))
    return random_str