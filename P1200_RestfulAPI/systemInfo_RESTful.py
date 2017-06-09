import requests
import json
from pprint import pprint #make the json file eazy to read
from time import sleep


url = "http://192.168.108.93/api/slot/0/sysInfo"
header = {'Content-Type':'application/json','Accept':'vdn.dac.v1'}

for i in range(100):
    r = requests.get(url, headers=header)
    data = r.json()
    answer  = str(i).zfill(3)
    answer += str('_') + str(data['slot'])
    answer += str('__') + str(data['sysInfo']['device'][0]['modelName'])
    answer += str('_') + str(data['sysInfo']['device'][0]['deviceName'])
    answer += str('_') + str(data['sysInfo']['device'][0]['deviceUpTime'])
    answer += str('_') + str(data['sysInfo']['device'][0]['firmwareVersion'])
    answer += str('__') + str(data['sysInfo']['network']['LAN']['lanMac'])
    answer += str('_') + str(data['sysInfo']['network']['LAN']['lanIp'])
    print(answer)
    #sleep(0.1)
    r = []

pprint(r.json())

