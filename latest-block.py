from web3 import Web3
from settings  import Infura_config_url

#test connection to infura
infura_web3 = Web3(Web3.HTTPProvider(Infura_config_url))
print(infura_web3.isConnected(), 'Connected to Infura successfully!!')

#get the info about the  latest block
#using the eth.getBlock() method and pass the 'latest' as the keyword
latest_block = infura_web3.eth.getBlock('latest')
print(latest_block)