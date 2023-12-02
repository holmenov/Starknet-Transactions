from loguru import logger
import questionary

from classes.Threads import Threads
from settings import QUANTITY_THREADS
from utils.all_modules import *
from utils.utils import get_wallets


def get_module():
    module = questionary.select(
        'Choose the module you want to start with:',
        choices=[
            questionary.Choice('1) Random modules', random_modules),
            questionary.Choice('2) Random low-cost modules', random_low_cost_modules),
            questionary.Choice('3) DMail', dmail_send),
            questionary.Choice('4) Mint public NFT', mint_public_nft),
            questionary.Choice('5) Deposit ZkLend', deposit_zklend),
            questionary.Choice('6) Withdraw ZkLend', withdraw_zklend),
            questionary.Choice('7) Increase allowance for Unframed', increase_allowance_unframed),
            questionary.Choice('8) Cancel order on Unframed', cancel_orders_unframed),
            questionary.Choice('9) Swap on JediSwap', swap_jediswap),
            questionary.Choice('10) Swap on 10KSwap', swap_10k),
            questionary.Choice('11) Transfer ETH on random address', eth_transfer),
        ],
        qmark='📌 ',
        pointer='✅ '
    ).ask()

    return module


def main():
    module = get_module()
    data = get_wallets()
    
    threads = Threads(data)
    threads.start_workers(module=module, max_workers=QUANTITY_THREADS)
    

if __name__ == '__main__':
    logger.add('logs.log')
    main()