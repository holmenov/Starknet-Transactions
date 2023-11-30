import json


with open('wallets.txt', 'r', encoding='utf-8') as file:
    WALLETS = [wallet.strip() for wallet in file]

with open('addresses.txt', 'r', encoding='utf-8') as file:
    ADDRESSES = [address.strip() for address in file]

with open('data/dmail/abi.json', 'r') as file:
    DMAIL_ABI = json.load(file)
    
with open('data/nft/abi.json', 'r') as file:
    NFT_ABI = json.load(file)

with open('data/erc20_Abi.json', 'r') as file:
    ERC20_ABI = json.load(file)

with open('data/zklend/abi.json', 'r') as file:
    ZKLEND_ABI = json.load(file)

with open('data/jediswap/abi.json', 'r') as file:
    JEDISWAP_ABI = json.load(file)
    
with open('data/10kswap/abi.json', 'r') as file:
    SWAP10K_ABI = json.load(file)

DMAIL_ADDRESS = 0x0454F0BD015E730E5ADBB4F080B075FDBF55654FF41EE336203AA2E1AC4D4309

UNFRAMED_ADDRESS = 0x51734077ba7baf5765896c56ce10b389d80cdcee8622e23c0556fb49e82df1b

ZKLEND_ADDRESS = 0x04c0a5193d58f74fbace4b74dcf65481e734ed1714121bdc571da345540efa05

JEDISWAP_ADDRESS = 0x041fd22b238fa21cfcf5dd45a8548974d8263b3a531a60388411c5e230f97023

SWAP10K_ADDRESS = 0x07a6f98c03379b9513ca84cca1373ff452a7462a3b61598f0af5bb27ad7f76d1

STARKNET_TOKENS = {
    'ETH': 0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7,
    'USDC': 0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8,
    'USDT': 0x68f5c6a61780768455de69077e07e89787839bf8166decfbf92b645209c0fb8,
    'DAI': 0x00da114221cb83fa859dbdb4c44beeaa0bb37c7537ad5ae66fe5e0efd20e6eb3
}