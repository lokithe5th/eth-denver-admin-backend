#from zksync2.signer.eth_signer import PrivateKeyEthSigner
#from eth_account import Account
import constants
from zksync2.module.module_builder import ZkSyncBuilder
import pymongo

# Create MongoDB connection and setup database and collection
#client = pymongo.MongoClient("mongodb+srv://lourens:"+constants.mongo_password+"@cluster0.iwy9lj6.mongodb.net/?retryWrites=true&w=majority")
#db = client.denver
#collection = db.transactions

# The params for the `eth.filter` call
filter_params = {
    "fromBlock": constants.BLOCK_START,
    "toBlock": constants.BLOCK_END,
    "address": constants.TOKEN_ADDRESS
    #"topics": [constants.TOPIC_TRANSFER]
}

# Setup the `zksync` client
zksync_web3 = ZkSyncBuilder.build("https://zksync2-testnet.zksync.dev")
# Create the filter
filter = zksync_web3.zksync.filter(filter_params)
# Fetch all the filter entries
logs = filter.get_all_entries()

print(logs)

# Simple iteration through the returned queries
for log in logs:
    fromAddress = zksync_web3.zksync.get_transaction(log['transactionHash'].hex())
    timestamp = zksync_web3.zksync.get_block(log['blockNumber'])
    print("Transaction#: ", log['transactionHash'].hex(), "Blocknumber: ", log['blockNumber'], "TimeStamp: ", timestamp['timestamp'], "From: ", fromAddress['from'], " To: 0x"+log['topics'][1].hex()[26:65], " Amount: ",int(log['topics'][2].hex(), 16))
    entry = {
        "transaction_hash": log['transactionHash'].hex(),
        "block_number": log['blockNumber'],
        "to": "0x"+log['topics'][1].hex()[26:65],
        "amount": str(int(log['topics'][2].hex(), 16))
    }
    # Insert into collection
    # Comment out if no username or password and running locally just to test
    #collection.insert_one(entry)