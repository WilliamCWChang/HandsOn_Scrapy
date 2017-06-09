import requests
import json
from pprint import pprint #make the json file eazy to read
from time import sleep
import logging

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1



url = "http://192.168.108.93/api/slot/0/io/do"
#header = {'Content-Type':'application/json','Accept':'vdn.dac.v1'}
header = {'Content-Type':'application/json','Accept':'vdn.dac.v1' , 'content-length':'503'}
datas = '{"slot":0,"io":{"do":[{"doIndex":0,"doMode":0,"doStatus":1},{"doIndex":1,"doMode":0,"doStatus":1},{"doIndex":2,"doMode":0,"doStatus":0},{"doIndex":3,"doMode":0,"doStatus":0},{"doIndex":4,"doMode":0,"doStatus":1},{"doIndex":5,"doMode":0,"doStatus":0},{"doIndex":6,"doMode":0,"doStatus":0},{"doIndex":7,"doMode":0,"doStatus":0}]}}'

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


#for i in range(10):
r = requests.put(url,headers=header, timeout=0.5, data=datas)
print("  ")
print(r.request.headers)
print("  ")
print(r.request.body)


print("  ")
print(r.content)

#data = r.json()
##answer  = str(i).zfill(3)
#print("  ")
#
#answer = str('_') + str(data['slot'])
#answer += str('__') + str(data['sysInfo']['device'][0]['modelName'])
#answer += str('_') + str(data['sysInfo']['device'][0]['deviceName'])
#answer += str('_') + str(data['sysInfo']['device'][0]['deviceUpTime'])
#answer += str('_') + str(data['sysInfo']['device'][0]['firmwareVersion'])
#answer += str('__') + str(data['sysInfo']['network']['LAN']['lanMac'])
#answer += str('_') + str(data['sysInfo']['network']['LAN']['lanIp'])
##answer += str('_') + r.headers['x-runtime']
#print(answer)
#sleep(0.01)



