#from zksync2.signer.eth_signer import PrivateKeyEthSigner
#from eth_account import Account
import constants
from zksync2.module.module_builder import ZkSyncBuilder
import time

filter_params = {
    "fromBlock": 200000,
    "toBlock": 230000,
    "address": constants.TOKEN_ADDRESS,
    "topics": [constants.TOPIC_TRANSFER]
}


#account = Account.from_key("PRIVATE_KEY")
zksync_web3 = ZkSyncBuilder.build("https://zksync2-testnet.zksync.dev")

chain_id = zksync_web3.zksync.filter(filter_params)
#signer = PrivateKeyEthSigner(account, chain_id)

time.sleep(2)

logs = chain_id.get_all_entries()

print(logs)

for log in logs:
    print(log['AttributeDict'])