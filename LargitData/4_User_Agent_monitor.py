from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/58.0.3029.96 Safari/537.36'
}
rs = requests.session()
url = 'https://www.stockdog.com.tw/stockdog/index.php?m=overview&sid=1101+%E5%8F%B0%E6%B3%A5'
res = rs.get(url, headers=headers)

m = re.findall('document.getElementById\(\'g\d+\'\).innerHTML=\'<iframe src=\"(.*?)\"', res.text)

res2 = rs.get("https://www.stockdog.com.tw/stockdog/" + m[0], headers=headers)
print(res2.text)
