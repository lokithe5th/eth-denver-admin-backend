import datetime
import requests
import json
import calendar
import constants
import pickle
#from web3 import Web3, HTTPProvider
from zksync2.module.module_builder import ZkSyncBuilder
import asyncio

# instantiate a web3 remote provider
w3 = ZkSyncBuilder.build("https://starknet-mainnet.infura.io/v3/915563693acc45ca8fb73b9d82a4535c")

async def getChain():
    chainId = await w3.zksync.zks_get_bridge_contracts
    print(chainId)

async def main():
    await getChain()

main()

if __name__ == "__main__":
    asyncio.run(main())
