from __future__ import print_function
import requests
from bs4 import BeautifulSoup
payload = {
'StartStation'  :'977abb69-413a-4ccf-a109-0272c24fd490',
'EndStation'    :'f2519629-5973-4d08-913b-479cce78a356',
'SearchDate'    :'2017/05/31',
'SearchTime'    :'10:00',
'SearchWay'     :'DepartureInMandarin'

}
res = requests.post("http://www.thsrc.com.tw/tw/TimeTable/SearchResult",
                   data = payload)
html = res.text

soup = BeautifulSoup(html, "html.parser")
obj = soup.select('.touch_table')
print(len(obj))
for item in obj:
    print(item.select('.column1')[0].text, end='\t')
    print(item.select('.column2')[0].text, end='\t')
    print(item.select('.column3')[0].text, end='\t')
    print(item.select('.column4')[0].text, end='\t')
    print(item.select('.Width1')[0].text.replace(u'\xa0', u' '), end='\n')





