#while 1 == 1 :
 #   import requests
 #   import time
 #   time.sleep(1)
 #   price = ("https://www.google.com/search?q=bitcoin&rlz=1C1ONGR_enIN954IN954&sxsrf=ALiCzsZVbJpl_mfuD8DyUkIq1qDpqY1ehg%3A1668072018843&ei=UsJsY9GPM_yR3LUP-YWv8AM&ved=0ahUKEwjRgJLBpKP7AhX8CLcAHfnCCz4Q4dUDCA8&uact=5&oq=bitcoin&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIECCMQJzIKCAAQsQMQgwEQQzIECAAQQzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgQIABBDMgoIABCxAxCDARBDMgQIABBDOgoIABBHENYEELADOgcIABCwAxBDSgQIQRgASgQIRhgAUMQMWMQMYNEOaAJwAXgAgAF4iAF4kgEDMC4xmAEAoAEByAEKwAEB&sclient=gws-wiz-serp")
 #   Text = requests.get(price).text
 #   value = Text.find("bitcoin")
 #  print(value)
#import requests
#import time
#import bs4
#from bs4 import BeautifulSoup 
#while True:
 #   time.sleep(2)
  #  price = requests.get("https://www.google.com/search?q=bitcoin&rlz=1C1ONGR_enIN954IN954&sxsrf=ALiCzsZVbJpl_mfuD8DyUkIq1qDpqY1ehg%3A1668072018843&ei=UsJsY9GPM_yR3LUP-YWv8AM&ved=0ahUKEwjRgJLBpKP7AhX8CLcAHfnCCz4Q4dUDCA8&uact=5&oq=bitcoin&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIECCMQJzIKCAAQsQMQgwEQQzIECAAQQzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgQIABBDMgoIABCxAxCDARBDMgQIABBDOgoIABBHENYEELADOgcIABCwAxBDSgQIQRgASgQIRhgAUMQMWMQMYNEOaAJwAXgAgAF4iAF4kgEDMC4xmAEAoAEByAEKwAEB&sclient=gws-wiz-serp").text
   # price = price.find('price')
    #Next = requests.get("https://www.google.com/search?q=bitcoin&rlz=1C1ONGR_enIN954IN954&sxsrf=ALiCzsZVbJpl_mfuD8DyUkIq1qDpqY1ehg%3A1668072018843&ei=UsJsY9GPM_yR3LUP-YWv8AM&ved=0ahUKEwjRgJLBpKP7AhX8CLcAHfnCCz4Q4dUDCA8&uact=5&oq=bitcoin&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIECCMQJzIKCAAQsQMQgwEQQzIECAAQQzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgQIABBDMgoIABCxAxCDARBDMgQIABBDOgoIABBHENYEELADOgcIABCwAxBDSgQIQRgASgQIRhgAUMQMWMQMYNEOaAJwAXgAgAF4iAF4kgEDMC4xmAEAoAEByAEKwAEB&sclient=gws-wiz-serp").text
    #Next = Next.find('Bitcoin')
   # print("Bitcoin price is " )
    #print(Next*70)
    #print("Price is ")
    #print(price*70)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
drive = webdriver.Chrome("D:\PYTHON.code\chromedriver.exe")
website = 'https://google.com'
drive.get('website')
time.sleep(5)