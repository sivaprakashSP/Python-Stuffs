from web3 import Web3
import json

gananche_url="http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(gananche_url))
print(w3.isConnected())