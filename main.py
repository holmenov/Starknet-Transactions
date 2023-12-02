import random
import sys
import time
from typing import Callable
from loguru import logger
import questionary
from concurrent.futures import ThreadPoolExecutor

from settings import DEBUG_MODE, QUANTITY_THREADS, RANDOM_WALLETS, THREAD_SLEEP_FROM, THREAD_SLEEP_TO
from utils.all_modules import *
from utils.utils import _async_run_module, get_wallets


def get_module():
    selected_module = questionary.select(
        'Choose the module you want to start with:',
        choices=[
            questionary.Choice('1) Random module', random_launch),
            questionary.Choice('2) DMail', dmail_send),
            questionary.Choice('3) Mint public NFT', mint_public_nft),
            questionary.Choice('4) Deposit on ZkLend', deposit_zklend),
            questionary.Choice('5) Increase allowance for Unframed', increase_allowance_unframed),
            questionary.Choice('6) Cancel order on Unframed', cancel_orders_unframed),
            questionary.Choice('7) Swap on JediSwap', swap_jediswap),
            questionary.Choice('8) Swap on 10KSwap', swap_10k),
            questionary.Choice('X) Close', 'exit')
        ],
        qmark='📌 ',
        pointer='✅ '
    ).ask()

    if selected_module == 'exit':
        sys.exit()
    return selected_module


def main(module: Callable):
    data = get_wallets()

    if RANDOM_WALLETS:
        random.shuffle(data)

    with ThreadPoolExecutor(max_workers=QUANTITY_THREADS) as executor:
        for _, account in enumerate(data, start=1):
            future = executor.submit(
                _async_run_module,
                module,
                account.get('id'),
                account.get('wallet'),
                account.get('address')
            )

            if DEBUG_MODE:
                exception = future.exception()
                exception_msg = (f'{account.get("id")} | {account.get("address")} | {exception}')
                logger.error(exception_msg) if exception else time.sleep(random.randint(THREAD_SLEEP_FROM, THREAD_SLEEP_TO))
            else:
                time.sleep(random.randint(THREAD_SLEEP_FROM, THREAD_SLEEP_TO))


if __name__ == '__main__':
    logger.add('logging.log')
    module = get_module()
    main(module)