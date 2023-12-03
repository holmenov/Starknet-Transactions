
from concurrent.futures import ThreadPoolExecutor
import random
import time
from typing import Callable
from loguru import logger

from settings import DEBUG_MODE, RANDOM_WALLETS, THREAD_SLEEP_FROM, THREAD_SLEEP_TO
from utils.utils import _async_run_module


class Threads:
    def __init__(self, data: list) -> None:
        self.data = data
        
        if RANDOM_WALLETS:
            random.shuffle(self.data)
    
    def start_workers(self, module: Callable, max_workers: int):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for account in self.data:
                executor.submit(
                    _async_run_module, module, account.get('id'), account.get('wallet'), account.get('address')
                )
                time.sleep(random.randint(THREAD_SLEEP_FROM, THREAD_SLEEP_TO))