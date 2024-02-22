# ==========================================================
#                       MAIN SETTINGS
# ==========================================================


class MainSettings:
    # Gwei control
    MAX_GAS = 40

    # Take the wallets in random order
    RANDOM_WALLETS = True

    # Remove wallet from files after work
    REMOVE_WALLET = True

    # StarkNet node, you can change this
    STARKNET_NODE = 'https://starknet-mainnet.public.blastapi.io'

    # Period in seconds to run all wallets
    START_PERIOD_FROM = 1
    START_PERIOD_TO = 600

    # Module repetitions for each wallet
    REPEATS_PER_WALLET = 1

    # Sleeps after work
    SLEEP_AFTER_WORK_FROM = 60 # Seconds
    SLEEP_AFTER_WORK_TO = 120 # Seconds

    # Slippage for swaps
    SLIPPAGE = 3


# ===========================================================
#                       MODULES SETTINGS
# ===========================================================


# nft_contract - NFT Contract Address (for public mint NFT)
# min_amount, max_amount - Minimum and maximum amount for transactions
# decimals - Number of digits for rounding after the decimal point
# all_amount - Use a percentage of the balance for the transaction
# min_percent, max_percent - Minimum and maximum percentage of the balance for the transaction
# swap_reverse - Reverse swap with the same parameters


class ModulesSettings:

    class MintPublicNFT:
        nft_contract = 0x00b719f69b00a008a797dc48585449730aa1c09901fdbac1bc94b3bdc287cf76

    class ZkLend:
        min_amount = 0.0005
        max_amount = 0.0009
        decimals = 5
        
        withdraw = True

    class Unframed:
        class IncreaseAllowance:
            min_amount = 0.00001
            max_amount = 0.00009
            decimals = 6

    class JediSwap:
        from_token = 'ETH'
        to_token = 'USDC'

        min_amount = 0.0005
        max_amount = 0.0009
        decimals = 5

        all_amount = False
        min_percent = 10
        max_percent = 20

        swap_reverse = True

    class Swap10K:
        from_token = 'ETH'
        to_token = 'USDC'

        min_amount = 0.0005
        max_amount = 0.0009
        decimals = 5

        all_amount = False
        min_percent = 10
        max_percent = 20

        swap_reverse = True

    class Transfer:
        class RandomTransfer:
            min_amount = 0.00002
            max_amount = 0.00008
            decimals = 6
        class TransferCEX:
            min_percent = 100
            max_percent = 100