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
#path = 'practise.json'
driver = webdriver.Chrome("D:\PYTHON.code\chromedriver.exe")
driver.get("https://sves.org.in/ecap/StudentMaster.aspx")
User_Name = '22A81A0639'
Pass = 'Madhan#4332'
User_Name_Input = driver.find_element(By.XPATH,'//*[@id="txtId2"]')
User_Name_Input.send_keys(User_Name)
Pass_Input = driver.find_element(By.XPATH,'//*[@id="txtPwd2"]')
Pass_Input.send_keys(Pass)
Submit = driver.find_element(By.XPATH,'//*[@id="imgBtn2"]')
Submit.click()
time.sleep(4)
link = driver.find_element(By.XPATH,'//*[@id="tblReport"]/h1[2]')
if link == True :
    print("IT is here")
else print()
#Performance = driver.find_element(By.XPATH,'//*[@id="tblReport"]/h1[2]')
#Div_Element = By.XPATH,'//*[@id="divProfile_Present"]'
#Attendance = Performance.find_element(Div_Element)
#Attendance_Percentage = Attendance.find_element(By.XPATH,'//*[@id="divProfile_Present"]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/center/div/table/tbody/tr[1]/td/table/tbody/tr[10]/td[4]').text
#time.sleep(4)
#print(Attendance_Percentage)
driver.quit()
