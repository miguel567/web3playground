
from web3 import Web3, HTTPProvider

host = 'laptop'
kovan_port = '8555'
mainnet_port = '8555'
hostname = 'http://'+host+':'+kovan_port
w3 = Web3(HTTPProvider(hostname))

print(w3.clientVersion)

