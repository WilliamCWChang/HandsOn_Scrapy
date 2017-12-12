from __future__ import print_function
from bs4 import BeautifulSoup
from time import sleep

import requests
count = 0
url = 'http://192.168.108.184/05_21.htm?CHANNEL_NO=0'
# url = 'http://192.168.108.185/05_41.htm?CHANNEL_NO=0'
print("=== Start ====================")
while 1:
    count = count + 1
    res = requests.get(url)
    bs = BeautifulSoup(res.content, "html.parser")
    token = bs.find("input", {"name": "token"})
    token_value = str(token).split(">")[0]
    print("{0} - {1}".format(count, token_value))
    # sleep(1)
