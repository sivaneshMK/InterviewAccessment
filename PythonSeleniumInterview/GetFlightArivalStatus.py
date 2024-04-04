'''
Created By: sivanesh,
Contact: 9087394995

'''
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

#To Start a ChromeBrowser
driver = webdriver.Chrome()

#To launch The URL
driver.get("https://www.flightradar24.com/data/airports/pnq")
driver.maximize_window()
time.sleep(5)

flag= False
popup = ""

#If Continue popup is not displayed it will prin the message
# if popup is displayed it will click on the continue button
try:
    popup = driver.find_element(By.XPATH, "//button[text()='Continue']")
    flag=popup.is_displayed()
except:
    flag =True

if flag==True:
    popup.click()
else:
    print("The popup is not visible")
time.sleep(5)

#To perform pagedown operation to see the table
driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#List of from locations to check
From = ["Bangaluru", "Delhi", "Goa", "Chandigarh", "Hyderabad", "Nagpur", "Dubai"]

# iterate each and every location and get status of the arival
# if location is not in the table it will print the message
for i in From:
    xpath = "//div[@class='row cnt-schedule-table']/table/tbody/tr[@class='hidden-xs hidden-sm ng-scope']/td/div/span[contains(text(),'"+i+"')]//ancestor::td//following-sibling::td[4]"
    try:
        text = driver.find_element(By.XPATH, xpath).text
        print(i+": "+text)
    except NoSuchElementException:
        print("The Location "+i+" is Not available in the table")