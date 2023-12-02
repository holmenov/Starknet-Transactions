# MODULE SETTINGS

# nft_contract - NFT Contract Address (for public mint NFT)
# min_amount, max_amount - Minimum and maximum amount for transactions
# decimals - Number of digits for rounding after the decimal point
# all_amount - Use a percentage of the balance for the transaction
# min_percent, max_percent - Minimum and maximum percentage of the balance for the transaction
# swap_reverse - Reverse swap with the same parameters

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
    min_amount = 0.0005
    max_amount = 0.0009
    decimals = 5