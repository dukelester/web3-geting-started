from web3.auto import w3

my_web3 = w3()
print(my_web3.isConnected(), 'connected via HTTP and Geth locally')