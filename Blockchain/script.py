from web3 import Web3
import json
gananche_url="http://127.0.0.1:7545"

w3 = Web3(Web3.HTTPProvider(gananche_url))

#print(w3.eth.accounts)

abi=json.loads('[{"inputs":[{"internalType":"int256","name":"a","type":"int256"},{"internalType":"uint256","name":"b","type":"uint256"},{"internalType":"string","name":"c","type":"string"}],"name":"getinput","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"retrieve","outputs":[{"internalType":"int256","name":"","type":"int256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]')

address="0x5B395FB162AFc4cd53E80DCE11f451Ba10e7876E"
w3.eth.defaultAccount=w3.eth.accounts[0]

contract=w3.eth.contract(address=address,abi=abi) 

contract.functions.getinput(-32,32,"Siva").transact()

print(contract.functions.retrieve().call())