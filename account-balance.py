from web3 import Web3
from sett.settings  import Infura_config_url

print(Infura_config_url) #check the url
web3 = Web3(Web3.HTTPProvider(Infura_config_url))
print(web3.isConnected(), 'connected via HTTP and Infura')

blockNumber = web3.eth.blockNumber #get the latest block number
print(blockNumber, 'block number')

balance = web3.eth.getBalance('0x52bc44d5378309EE2abF1539BF71dE1b7d7bE3b5') #get the balance of the account
print(balance, 'balance in Wei')
#convert the balance to wei
new_balance = web3.fromWei(balance, 'ether')
print(new_balance, 'balance in ether')

