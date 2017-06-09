import requests
import re #for split the string eazy.
from time import sleep

url = "http://192.168.102.142/getParam.cgi"
params = {}
params.update({'S0_MN': '?'})
params.update({'S0_DN': '?'})
params.update({'S0_DDT': '?'})
params.update({'S0_DTZ': '?'})
params.update({'S0_DUT': '?'})
params.update({'S0_FV': '?'})
params.update({'S0_SN': '?'})
params.update({'S0_LMAC': '?'})
params.update({'S0_LIP': '?'})


#data = ",".join(map(str, params + '=' + params[param]))
#print(data)


if params:
    print(url)
    line = 1
    for param in params:
        if line:
            url +="?"
            line =0
        else:
            url += "&"
        url += ( param + '=' + params[param])
        print(url)



#for i in range(100):
r = requests.get(url)
#    data = r.json()
#    answer  = str(i).zfill(3)
#    answer += str('_') + str(data['slot'])
#    answer += str('__') + str(data['sysInfo']['device'][0]['modelName'])
#    answer += str('_') + str(data['sysInfo']['device'][0]['deviceName'])
#    answer += str('_') + str(data['sysInfo']['device'][0]['deviceUpTime'])
#    answer += str('_') + str(data['sysInfo']['device'][0]['firmwareVersion'])
#    answer += str('__') + str(data['sysInfo']['network']['LAN']['lanMac'])
#    answer += str('_') + str(data['sysInfo']['network']['LAN']['lanIp'])
data = r.text.split("\r\n")
print(data)

items = []
for item in data:
    if '=' in item:
        first, last= item.split("=")
        a,b = last.split("(")
        out = [first,a,b[:-1]]
        items.append(out)
        print(out)
print(items)







print()
#    #sleep(0.1)
#    r = []
#
#pprint(r.json())

