import asyncio
from typing import Callable

from utils.utils import async_sleep, remove_wallet_from_files
from settings import MainSettings as SETTINGS
from utils.wrappers import repeats


async def start_tasks(module: Callable, data: list):
    tasks = []

    for account in data:
        tasks.append(
            asyncio.create_task(_run_module(module, account.get('id'), account.get('wallet'), account.get('address')))
        )

    await asyncio.gather(*tasks)


async def _run_module(module: Callable, account_id: int, key: str, address: str):
    await async_sleep(
        SETTINGS.START_PERIOD_FROM, SETTINGS.START_PERIOD_TO,
        True, account_id, address, 'before starting work'
    )

    await run_module(module, account_id, key, address)

    if SETTINGS.REMOVE_WALLET:
        remove_wallet_from_files(key, address)


@repeats
async def run_module(module: Callable, account_id: int, key: str, address: str):
    succcess_bridge = await module(account_id, key, address)
    if not succcess_bridge: return False
    return True