import requests
import json
from pprint import pprint #make the json file eazy to read
from time import sleep

json_data={"slot":0,
            "io":{
                "ao":[
                    {"aoIndex":0,"aoMode":1,"aoValueRaw":50,"aoValueScaled":4},
                    {"aoIndex":1,"aoMode":1,"aoValueRaw":0,"aoValueScaled":4},
                    {"aoIndex":2,"aoMode":1,"aoValueRaw":50,"aoValueScaled":4},
                    {"aoIndex":3,"aoMode":1,"aoValueRaw":0,"aoValueScaled":4}
                    ]
                }
            }


def getRawdata(num):
    r = requests.get(url, headers=header)
    data = r.json()
    output  = str(num).zfill(5)
    for i in range(AO_number):
        output += str(' | ') + str(data['io']['ao'][i]['aoIndex'])
        output += str('_') + str(data['io']['ao'][i]['aoValueRaw']).zfill(6)
    print(output)
    sleep(0.1)
    r = []


def setRawdata(AO0, AO1, AO2, AO3):
    json_data['io']['ao'][0]['aoValueRaw'] = AO0
    json_data['io']['ao'][1]['aoValueRaw'] = AO1
    json_data['io']['ao'][2]['aoValueRaw'] = AO2
    json_data['io']['ao'][3]['aoValueRaw'] = AO3
    r = requests.put(url, headers=header, json = json_data)
    #print(json_data);




ip = "192.168.108.94"
command = "/api/slot/0/io/ao"
url = "http://" + ip + command
print("url = " + url)
AO_number = 4
header = {'Content-Type':'application/json','Accept':'vdn.dac.v1'}

raw_value = 1;
#for raw_value in range(0, 4096, 128):  #raw current/voltage range
while raw_value != 4095:
    raw_value *= 2;
    if raw_value > 4095:
        raw_value = 4095

    setRawdata(raw_value, raw_value, raw_value, raw_value)
    getRawdata(raw_value)
    sleep(3)

