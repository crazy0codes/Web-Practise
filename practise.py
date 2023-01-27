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
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the web driver
path = 'practise.json'
driver = webdriver.Chrome("D:\PYTHON.code\chromedriver.exe")
x = driver.get("https://www.google.com/search?q=bitcoin+price+&rlz=1C1ONGR_enIN954IN954&sxsrf=AJOqlzUQEyRyxqCrL7r4ctEZi6lN_Xon8w%3A1674823771812&ei=W8jTY7meMeLV4-EPv6C5-Aw&ved=0ahUKEwj5t-vf5Of8AhXi6jgGHT9QDs8Q4dUDCBA&uact=5&oq=bitcoin+price+&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIECCMQJzIFCAAQkQIyCwgAEIAEELEDEIMBMgoIABCxAxCDARBDMggIABCxAxCRAjIFCAAQkQIyCggAELEDEIMBEEMyCwgAEIAEELEDEIMBOgcIIxCwAxAnOgoIABBHENYEELADSgQIQRgASgQIRhgAUNACWNACYNEEaAFwAXgAgAHPAYgBzwGSAQMyLTGYAQCgAQHIAQnAAQE&sclient=gws-wiz-serp")
while True :
    price = driver.find_element(By.XPATH,'//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]').text
    data = {"price": price}
    open(path,'w').write(json.dumps(data))
    time.sleep(60)