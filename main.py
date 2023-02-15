#from zksync2.signer.eth_signer import PrivateKeyEthSigner
#from eth_account import Account
import constants
from zksync2.module.module_builder import ZkSyncBuilder
import time

filter_params = {
    "fromBlock": constants.BLOCK_START,
    "toBlock": constants.BLOCK_END,
    "address": constants.TOKEN_ADDRESS,
    "topics": [constants.TOPIC_TRANSFER]
}


#account = Account.from_key("PRIVATE_KEY")
zksync_web3 = ZkSyncBuilder.build("https://zksync2-testnet.zksync.dev")

transferTopic = zksync_web3.keccak(text = 'transfer(address,uint256)')
print(transferTopic.hex())

chain_id = zksync_web3.zksync.filter(filter_params)
#signer = PrivateKeyEthSigner(account, chain_id)

logs = chain_id.get_all_entries()

print(logs)

for log in logs:
    print("Transaction#: ", log['transactionHash'].hex(), " To: 0x"+log['topics'][1].hex()[26:65], " Amount: ",int(log['topics'][2].hex(), 16))