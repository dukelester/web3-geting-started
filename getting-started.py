from web3 import Web3, EthereumTesterProvider

web3 = Web3(EthereumTesterProvider())
print(web3.isConnected(), 'Node connected') #check if the node is connected

#connect to the node via geth

my_web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
print(my_web3.isConnected(), 'connected via HTTP and Geth locally')

#connect via websocket
# web3_socket = Web3(Web3.WebsocketProvider("wss://127.0.0.1:8546"))
# print(web3_socket.isConnected(), 'connected via websocket and Geth locally')

from web3.auto import w3
print(w3.isConnected(), 'Automatic connection')

#try to get the latest block in the node for my_web3
#not available locally of course
my_block = my_web3.eth.getBlock('latest')
print(my_block)

#get the keys using the eth.accounts property
my_keys = my_web3.eth.accounts
print(my_keys)