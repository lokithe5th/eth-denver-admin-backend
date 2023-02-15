import constants
#from web3 import Web3, HTTPProvider
from zksync2.module.module_builder import ZkSyncBuilder
import asyncio

# instantiate a web3 remote provider
w3 = ZkSyncBuilder.build("https://starknet-goerli2.infura.io/v3/915563693acc45ca8fb73b9d82a4535c")

def getChain():
    chainId = w3.zksync.chain_id
    print(chainId)

getChain()