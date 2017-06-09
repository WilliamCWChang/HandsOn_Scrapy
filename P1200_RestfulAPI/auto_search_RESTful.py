import argparse
import requests
import json
from pprint import pprint #make the json file eazy to read
from time import sleep

def channel_check_func(ip, channel_type):
    url = "http://" + ip + "/api/slot/0/io/" + channel_type
    header = {'Content-Type':'application/json','Accept':'vdn.dac.v1'}
    r = requests.get(url,headers=header, timeout=0.5)
    if r.status_code == 200:
        print('OK   : ' + channel_type + ' \'s restful API is detected ')
        return True
    else:
        print('ERROR: ErrorCode = ' + str(r.status_code) + ', No ' + channel_type)
        return False

def channel_num_check_func(ip, channel_type):
    url = "http://" + ip + "/api/slot/0/io/" + channel_type
    header = {'Content-Type':'application/json','Accept':'vdn.dac.v1'}
    r = requests.get(url,headers=header, timeout=0.5)
    data = r.json()
    channelNum = len(data['io'][channel_type])
    print(channel_type, end=" ")
    print("channel number = " + str(channelNum))
    return channelNum

def channel_status(ip, channel_type, channel_num):
    url = "http://" + ip + "/api/slot/0/io/" + channel_type
    header = {'Content-Type':'application/json','Accept':'vdn.dac.v1'}
    r = requests.get(url,headers=header, timeout=0.5)
    data = r.json()
    for num in range(channel_num):
        print(data['io'][channel_type][num])

class DeviceClass:
    def __init__(self):
        self.di     = False
        self.do     = False
        self.relay  = False
        self.ai     = False
        self.ao     = False
        self.rtd    = False
        self.tc     = False
        self.di_ChannelNum = 0
        self.do_ChannelNum = 0
        self.relay_ChannelNum = 0
        self.ai_ChannelNum = 0
        self.ao_ChannelNum = 0
        self.rtd_ChannelNum = 0
        self.tc_ChannelNum = 0

#arg input
parser = argparse.ArgumentParser(description='example 192.168.108.93')
parser.add_argument('ip', action="store")
#parser.add_argument('name', action="store")
arg = parser.parse_args()


print('Connect to ' + arg.ip + ' finish!')

#if arg.name == 'E1213':
#    device = DeviceClass(True,True,False,False,False,False,False)
#else :
#    print("No this device")


device = DeviceClass()
device.di = channel_check_func(arg.ip, 'di')
device.do = channel_check_func(arg.ip, 'do')
device.relay = channel_check_func(arg.ip, 'relay')
device.ai = channel_check_func(arg.ip, 'ai')
device.ao = channel_check_func(arg.ip, 'ao')
device.rtd = channel_check_func(arg.ip, 'rtd')
device.tc = channel_check_func(arg.ip, 'tc')
sleep(1)


#read the system infomation
#attrs = vars(device)
# {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
# now dump this in some way or another
#print (', '.join("%s: %s" % item for item in attrs.items()))

if device.di == True:
    di_ChannelNum = channel_num_check_func(arg.ip, 'di')
if device.do == True:
    do_ChannelNum = channel_num_check_func(arg.ip, 'do')
if device.relay == True:
    relay_ChannelNum = channel_num_check_func(arg.ip, 'relay')
if device.ai == True:
    ai_ChannelNum = channel_num_check_func(arg.ip, 'ai')
if device.ao == True:
    ao_ChannelNum = channel_num_check_func(arg.ip, 'ao')
if device.rtd == True:
    rtd_ChannelNum = channel_num_check_func(arg.ip, 'rtd')
if device.tc == True:
    tc_ChannelNum = channel_num_check_func(arg.ip, 'tc')
sleep(1)



url = "http://" + arg.ip + "/api/slot/0/sysInfo"
header = {'Content-Type':'application/json','Accept':'vdn.dac.v1'}
r = requests.get(url,headers=header, timeout=0.5)
data = r.json()
answer = str(data['slot'])
answer += str('__') + str(data['sysInfo']['device'][0]['modelName'])
answer += str('_') + str(data['sysInfo']['device'][0]['deviceName'])
answer += str('_') + str(data['sysInfo']['device'][0]['deviceUpTime'])
answer += str('_') + str(data['sysInfo']['device'][0]['firmwareVersion'])
answer += str('__') + str(data['sysInfo']['network']['LAN']['lanMac'])
answer += str('_') + str(data['sysInfo']['network']['LAN']['lanIp'])
print(answer)
sleep(1)


if device.di == True:
    channel_status(arg.ip, 'di', di_ChannelNum)
if device.do == True:
    channel_status(arg.ip, 'do', do_ChannelNum)
if device.relay == True:
    channel_status(arg.ip, 'relay', relay_ChannelNum)
if device.ai == True:
    channel_status(arg.ip, 'ai', ai_ChannelNum)
if device.ao == True:
    channel_status(arg.ip, 'ao', ao_ChannelNum)
if device.rtd == True:
    channel_status(arg.ip, 'rtd', rtd_ChannelNum)
if device.tc == True:
    channel_status(arg.ip, 'tc', tc_ChannelNum)









'''
url = "http://" + arg.ip + "/api/slot/0/sysInfo"
#url = "http://192.168.108.93/api/slot/0/sysInfo"
header = {'Content-Type':'application/json','Accept':'vdn.dac.v1'}

for i in range(10):
    r = requests.get(url,headers=header, timeout=0.5)
    data = r.json()
    answer  = str(i).zfill(3)
    answer = str('_') + str(data['slot'])
    answer += str('__') + str(data['sysInfo']['device'][0]['modelName'])
    answer += str('_') + str(data['sysInfo']['device'][0]['deviceName'])
    answer += str('_') + str(data['sysInfo']['device'][0]['deviceUpTime'])
    answer += str('_') + str(data['sysInfo']['device'][0]['firmwareVersion'])
    answer += str('__') + str(data['sysInfo']['network']['LAN']['lanMac'])
    answer += str('_') + str(data['sysInfo']['network']['LAN']['lanIp'])
    print(answer)
    sleep(0.01)
    r = []
'''

