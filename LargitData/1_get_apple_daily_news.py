import requests
web_url = "http://www.appledaily.com.tw/realtimenews/section/new/"
res = requests.get(web_url)
print res
print res.text

