from bs4 import BeautifulSoup as bs
import pandas as pd
import codecs
import re
import requests
import time
from random import choice
from selenium import webdriver
# # G = open(r"C:\Users\Vitya\Desktop\py\parser\my.txt" , encoding='UTF-8')
# with open(r"C:\Users\Vitya\Desktop\py\parser\my.txt", "r" , encoding='UTF-8') as f:
#     outList = re.findall(r"https://steamcommunity.com/[^\",;]*" , f.read())         # Получаем список со ссылками на предметы 
# # print(outList)
# outList = outList[0:110]                                                            # Обрезаем конец списка для быстродействия
# print(len(outList))
# i=0
# f.close()
# with open(r"C:\Users\Vitya\Desktop\py\parser\outList.txt", "w" ) as f1:
#      f1.write("")                                                                   # Удаляем содержимое outList

# useragents = open(r"C:\Users\Vitya\Desktop\py\parser\useragents.txt", "r" ).read().split('\n')
# proxies = open(r"C:\Users\Vitya\Desktop\py\parser\proxy1.txt", "r" ).read().split('\n')

# proxy = {'http': 'http://' + choice(proxies)}
# useragent = {'User-Agent': choice(useragents)} 

driver = webdriver.Chrome(executable_path=  r'C:\Users\Vitya\Desktop\py\parser\chromedriver\chromedriver.exe')
seleniumUrl = 'https://smallseotools.com/ru/free-proxy-list/'
try:
    driver.get(url= seleniumUrl)
    time.sleep(10)
except Exception as ex:
    print(ex)   
finally:
    driver.close()
    driver.quit()    

# print('Proxy - ' , end ="")
# print(proxy)
# print('UserAgent - ' , end ="")
# print(useragent)

# with open(r"C:\Users\Vitya\Desktop\py\parser\proxy.txt", "w" ) as f1:
#     f1.write (str(requests.get('https://smallseotools.com/ru/free-proxy-list/' , headers = useragent, proxies=proxy)))

       



# for items in outList:
#     url_of_items = items
#     r = requests.get(url_of_items)
#     soup = bs(r.text, "html.parser")
#     prices = soup.find_all('div', class_="searchRe")                     # Находим все div'ы с нужными классами 
#     i = i+1
#     # time.sleep(1)
#     print(str(round(i/len(outList)*100 , 2)) + ' %')
#     with open(r"C:\Users\Vitya\Desktop\py\parser\outList.txt", "a" , encoding='UTF-8') as f1:
#          f1.write(str(prices))                                                      # Записывам всё содержимое div'ов в outList
         









