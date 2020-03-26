
from web3 import Web3, HTTPProvider
import os, env

""" setting up hosts to fetch data """
kovanHostname = 'http://'+os.getenv('localhost')+':'+os.getenv('kovan_port')
mainnetHostname = 'http://'+os.getenv('localhost')+':'+os.getenv('mainnet_port')



""" fetcing infura Mainnet data """
w3realMainnet = Web3(HTTPProvider(os.getenv('realHost')))
realMainnetBlockNumber = w3realMainnet.eth.blockNumber


""" fetching local Mainnet node data """
w3localMainnet = Web3(HTTPProvider(mainnetHostname))
localMainnetBlockNumber = w3localMainnet.eth.blockNumber

print('Real Mainnet blocknumber:', realMainnetBlockNumber, 'Local mainnet blocknumber:', localMainnetBlockNumber, 'Local is behind', realMainnetBlockNumber-localMainnetBlockNumber)


""" fetcing infura Mainnet data """
w3realMainnet = Web3(HTTPProvider(os.getenv('kovanHost')))
realKovanBlockNumber = w3realMainnet.eth.blockNumber

""" fetching Kovan Mainnet node data """
w3localKovan = Web3(HTTPProvider(kovanHostname))
localKovanBlockNumber = w3localKovan.eth.blockNumber

print('Real Kovan blocknumber:', realKovanBlockNumber, 'Local Kovan blocknumber:', localKovanBlockNumber, 'Local is behind', realKovanBlockNumber-localKovanBlockNumber)