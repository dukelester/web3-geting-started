from web3 import Web3
from sett.settings  import Infura_config_url

#test connection to infura
infura_web3 = Web3(Web3.HTTPProvider(Infura_config_url))
print(infura_web3.isConnected(), 'Connected to Infura successfully!!')

#get the info about the  latest block
#using the eth.getBlock() method and pass the 'latest' as the keyword
latest_block = infura_web3.eth.getBlock('latest')
print(latest_block)

#get the transactions that are in the latest block
latest_tranc = infura_web3.eth.get_balance('0x9869b14233B48968bBCc612A570BF70b42AcFDB0')
print(latest_tranc)

#get block transactions
block_tranc = infura_web3.eth.get_block_transaction_count()
print(block_tranc)