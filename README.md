![](https://www.starknet.io/assets/sn_logo_banner.png)

---

With this repository, you can do simple transactions on **StarkNet**. You can do actions such as:

- Send mail via Dmail
- Mint public NFT
- Deposit and withdraw on ZkLend
- Increase allowance for Unframed
- Swap on JediSwap
- Swap on 10KSwap
- Random select any modules

## INSTALLATION

1. Install **Python 3.11+**.
2. `git clone https://github.com/holmenov/Starknet-Transactions.git`.
3. `cd Starknet-Transactions`.
4. `pip install -r requirements.txt`.

## SETUP

1. Insert private keys into `wallets.txt`
2. Insert wallet addresses in `addresses.txt`
3. Set the settings in `settings.py` *(Check SETTIGNS section)*
4. Set the settings for each module in `modules_settings.py` 

## SETTINGS

- `MAX_GAS` - Maximum GAS in GWEI for transactions [Integer].
- `RANDOM_WALLET` - Random wallet mode [Boolean].
- `DEBUG_MODE` - Developer mode for bug tracking [Boolean].
- `STARKNET_NODE` - Node for StarkNet [String].
- `QUANTITY_THREADS` - Quantity threads [Integer].
- `THREAD_SLEEP_FROM`, `THREAD_SLEEP_TO` - Interval in seconds between thread starts [Integer].
- `SLEEP_AFTER_WORK_FROM`, `SLEEP_AFTER_WORK_TO` - Seconds to sleep after completing a task [Integer].
- `SLIPPAGE` - Percentage that is lost on exchange [Integer].