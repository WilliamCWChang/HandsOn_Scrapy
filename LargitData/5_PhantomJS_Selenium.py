from __future__ import print_function
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import sys

browser = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
#browser = webdriver.Firefox()

browser.get("https://www.agoda.com/pages/agoda/default/DestinationSearchResult.aspx?asq=zWuVSTFwAmUZtJhrjzSYy5ufa9Vwpz6XltTHq4n%2B9gMYSfr7u1CU1i2lx00TDWH67lxWsQ6v%2FrbtGwzAUB%2FtOU%2FdDeCkxleINu%2BSBVhHZM%2BIpGI3GSP9dWr%2F8u9MCc9T2OGPRUf%2FnqWVFuWaH2y7CrS7mFrDxsW1r6%2BWtQtj5qO6pb0fC98X0j%2F7ua2%2FHygyWaTGybgLZnzu83SuX64zYXSk%2FM8eVuQYqDHVLhv%2F6oNjjoTmpFlSkVcSfnu9ryzz4KE%2FoYnM%2Fefy83sE%2FJDBPA%3D%3D&city=4951&cid=1732641&tag=41460a09-3e65-d173-1233-629e2428d88e&gclid=Cj0KEQjwxbDIBRCL99Wls-nLicoBEiQAWroh6uLlQWnHWRlc9Euu6Pg_XC1NRtBzj5Yb8HkVs-MjQLMaAigh8P8HAQ&tick=636295974842&txtuuid=c48ab805-f9ed-45d4-bb4a-2377625889d9&pagetypeid=103&origin=TW&aid=81837&userId=5fcd3f05-8c16-4426-acdf-5ee6bb07f69f&languageId=20&sessionId=xhjywu5gunsz0c5oexhquovf&storefrontId=3&currencyCode=TWD&htmlLanguage=zh-tw&trafficType=User&cultureInfoName=zh-TW&textToSearch=%E5%8F%B0%E5%8C%97%E5%B8%82&guid=c48ab805-f9ed-45d4-bb4a-2377625889d9&isHotelLandSearch=true&checkIn=2017-05-14&checkOut=2017-05-15&los=1&rooms=1&adults=2&children=0&ckuid=5fcd3f05-8c16-4426-acdf-5ee6bb07f69f&priceCur=TWD&hotelReviewScore=5")

soup = BeautifulSoup(browser.page_source, "html.parser")
while len(soup.select('.btn.btn-right')) > 0:
    for ele in soup.select('.hotel-info h3'):
        print(ele.text)
        # print(ele.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
        browser.find_element_by_id("paginationNext").click()
        time.sleep(3)
        soup = BeautifulSoup(browser.page_source)
browser.close()


