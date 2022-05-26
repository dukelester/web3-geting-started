#connecting to Infura via HTTPs
from web3 import Web3
from sett.settings import Infura_config_url
infura_connection = Web3(Web3.HTTPProvider(Infura_config_url))

print(infura_connection.isConnected(), 'connected via HTTP and Infura')
