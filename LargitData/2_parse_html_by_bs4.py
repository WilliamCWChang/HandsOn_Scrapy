from __future__ import print_function
import requests
from bs4 import BeautifulSoup
web_url = "http://www.appledaily.com.tw/realtimenews/section/new/"
res = requests.get(web_url)
print("check = " + str(res))

html = res.text
# print res.text

soup = BeautifulSoup(html, "html.parser")
# do not have <tag>
# print soup.text
# contain in a list and display tags
# print soup.contents
# print soup.select('html')[0]
for item in  soup.select('.rtddt'):
    #print item.select('time')[0].encode('utf8'),
    print(item.select('time')[0].text, end='\t')
    print(item.select('h2')[0].text, end='\t')
    print(item.select('font')[0].text)

