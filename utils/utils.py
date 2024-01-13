import random
import string
import sys
from loguru import logger
import asyncio

from utils.config import ADDRESSES, WALLETS


def send_logs(msg: str, account_id: int, address: str, status: str = 'info'):
    if status == 'info':
        logger.info(f'Account №{account_id} | {address} | {msg}')
    elif status == 'success':
        logger.success(f'Account №{account_id} | {address} | {msg}')
    elif status == 'error':
        logger.error(f'Account №{account_id} | {address} | {msg}')
    else:
        logger.debug(f'Account №{account_id} | {address} | {msg}')


async def async_sleep(sleep_from: int, sleep_to: int, logs: bool = True, account_id: int = 0, address: str = '', msg: str = ''):
    delay = random.randint(sleep_from, sleep_to)
    
    if logs:
        if not msg:
            logger.info(f'Account №{account_id} | {address} | Sleep {delay} seconds.')
        else:
            logger.info(f'Account №{account_id} | {address} | Sleep {delay} seconds, {msg}.')

    for _ in range(delay): await asyncio.sleep(1)


def get_wallets():
    if len(WALLETS) != len(ADDRESSES):
        logger.error('The number of wallets and addresses do not match')
        sys.exit()

    elif len(WALLETS) < 1:
        logger.error('It seems you forgot to enter the wallets')
        sys.exit()

    data = [{'id': id, 'wallet': wallet, 'address': address} for id, (wallet, address) in enumerate(zip(WALLETS, ADDRESSES), start=1)]

    return data


def get_random_string() -> str:
    letters = string.ascii_lowercase + string.digits
    length = random.randint(2, 4)
    random_str = ''.join(random.choice(letters) for _ in range(length))
    return random_str


def remove_wallet_from_files(wallet_to_remove: str, address_to_remove: str):
    with open('wallets.txt', 'r', encoding='utf-8') as wallets_file:
        wallets = wallets_file.readlines()
    with open('addresses.txt', 'r', encoding='utf-8') as addresses_file:
        addresses = addresses_file.readlines()
    
    cleared_wallets = [wallet for wallet in wallets if wallet.strip() != wallet_to_remove]
    cleared_addresses = [address for address in addresses if address.strip() != address_to_remove]
    
    with open('wallets.txt', 'w', encoding='utf-8') as wallets_file:
        wallets_file.writelines(cleared_wallets)
    with open('addresses.txt', 'w', encoding='utf-8') as addresses_file:
        addresses_file.writelines(cleared_addresses)