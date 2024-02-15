![](https://www.starknet.io/assets/sn_logo_banner.png)

---

With this repository, you can do simple transactions on **StarkNet**. You can do actions such as:

- Send mail via Dmail
- Mint public NFT
- Deposit and withdraw on ZkLend
- Increase allowance for Unframed
- Cancel orders on Unframed
- Swap on JediSwap
- Swap on 10KSwap
- Transfer ETH to random address
- Random select any modules

## INSTALLATION

1. Install **Python 3.11+**.
2. `git clone https://github.com/holmenov/Starknet-Transactions.git`.
3. `cd Starknet-Transactions`.
4. `pip install -r requirements.txt`.

## SETUP

1. Insert private keys into `wallets.txt`.
2. Insert wallet addresses in `addresses.txt`.
3. Set the settings in `settings.py`.
4. Insert your CEX Wallets address in `wallet_cex.txt` (Optional).

## SETTINGS

- `MAX_GAS` - Maximum GAS in GWEI for transactions [Integer].
- `RANDOM_WALLET` - Random wallet mode [Boolean].
- `REMOVE_WALLET` - Remove wallet after work [Boolean].
- `STARKNET_NODE` - Node for StarkNet [String].
- `START_PERIOD_FROM`, `START_PERIOD_TO` - Period in seconds to run all wallets [Integer].
- `REPEATS_PER_WALLET` - Module repetitions for each wallet [Integer].
- `SLEEP_AFTER_WORK_FROM`, `SLEEP_AFTER_WORK_TO` - Seconds to sleep after completing a task [Integer].
- `SLIPPAGE` - Percentage that is lost on exchange [Integer].

## MODULES SETTINGS

You can set different settings for each module.

- `nft_contract` - NFT Contract Address (for public mint NFT).
- `min_amount`, max_amount - Minimum and maximum amount for transactions.
- `decimals` - Number of digits for rounding after the decimal point.
- `all_amount` - Use a percentage of the balance for the transaction.
- `min_percent`, max_percent - Minimum and maximum percentage of the balance for the transaction.
- `swap_reverse` - Reverse swap with the same parameters.

There are also other settings that are individual to each module.