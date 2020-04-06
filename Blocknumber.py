
from web3 import Web3, HTTPProvider
import os, env, datetime

""" define NOW time stamp """
now =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

""" Define log file """
logFile=open("behind.log", "a+")
csvLogFile=open("behindlogs.csv", "a+")


""" setting up hosts to fetch data """
kovanHostname = 'http://'+os.getenv('localhost')+':'+os.getenv('kovan_port')
mainnetHostname = 'http://'+os.getenv('localhost')+':'+os.getenv('mainnet_port')



""" fetcing infura Mainnet data """
w3realMainnet = Web3(HTTPProvider(os.getenv('realHost')))
realMainnetBlockNumber = w3realMainnet.eth.blockNumber


""" fetching local Mainnet node data """
w3localMainnet = Web3(HTTPProvider(mainnetHostname))
try:
    localMainnetBlockNumber = w3localMainnet.eth.blockNumber
    print(now,' - Real Mainnet blocknumber:', realMainnetBlockNumber, 'Local mainnet blocknumber:', localMainnetBlockNumber, 'Local is behind:', realMainnetBlockNumber-localMainnetBlockNumber)
    logFile.write(str(now)+' - Real Mainnet blocknumber: '+str(realMainnetBlockNumber)+' Local mainnet blocknumber: '+str(localMainnetBlockNumber)+' Local is behind: '+str(realMainnetBlockNumber-localMainnetBlockNumber)+'\r\n')
    csvLogFile.write(str(now)+',mainnet,'+str(realMainnetBlockNumber)+','+str(localMainnetBlockNumber)+','+str(realMainnetBlockNumber-localMainnetBlockNumber)+'\r\n')
except Exception as ex:
    print('Host not available')
""" fetcing infura Mainnet data """
w3realMainnet = Web3(HTTPProvider(os.getenv('kovanHost')))
realKovanBlockNumber = w3realMainnet.eth.blockNumber

""" fetching Kovan Mainnet node data """
w3localKovan = Web3(HTTPProvider(kovanHostname))
try:
    localKovanBlockNumber = w3localKovan.eth.blockNumber
    print(now,' - Real Kovan blocknumber:', realKovanBlockNumber, 'Local Kovan blocknumber:', localKovanBlockNumber, 'Local is behind:', realKovanBlockNumber-localKovanBlockNumber)
    logFile.write(str(now)+' - Real Kovan blocknumber:'+str(realKovanBlockNumber)+'Local Kovan blocknumber:'+str(localKovanBlockNumber)+'Local is behind:'+str(realKovanBlockNumber-localKovanBlockNumber)+'\r\n')
    csvLogFile.write(str(now)+',kovan,'+str(realKovanBlockNumber)+','+str(localKovanBlockNumber)+','+str(realKovanBlockNumber-localKovanBlockNumber)+'\r\n')
except Exception as ex:
    print ('Host not available')


    logFile.close()
    csvLogFile.close()
