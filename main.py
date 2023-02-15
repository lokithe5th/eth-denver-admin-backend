#from zksync2.signer.eth_signer import PrivateKeyEthSigner
#from eth_account import Account
import constants
from zksync2.module.module_builder import ZkSyncBuilder
import pymongo


client = pymongo.MongoClient("mongodb+srv://lourens:"+constants.mongo_password+"@cluster0.iwy9lj6.mongodb.net/?retryWrites=true&w=majority")
db = client.denver
collection = db.transactions


filter_params = {
    "fromBlock": constants.BLOCK_START,
    "toBlock": constants.BLOCK_END,
    "address": constants.TOKEN_ADDRESS,
    "topics": [constants.TOPIC_TRANSFER]
}


#account = Account.from_key("PRIVATE_KEY")
zksync_web3 = ZkSyncBuilder.build("https://zksync2-testnet.zksync.dev")
filter = zksync_web3.zksync.filter(filter_params)
logs = filter.get_all_entries()

print(logs)

for log in logs:
    print("Transaction#: ", log['transactionHash'].hex(), "Blocknumber: ", log['blockNumber'], " To: 0x"+log['topics'][1].hex()[26:65], " Amount: ",int(log['topics'][2].hex(), 16))
    entry = {
        "transaction_hash": log['transactionHash'].hex(),
        "block_number": log['blockNumber'],
        "to": "0x"+log['topics'][1].hex()[26:65],
        "amount": str(int(log['topics'][2].hex(), 16))
    }

    collection.insert_one(entry)