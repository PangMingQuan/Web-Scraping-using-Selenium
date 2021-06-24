from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import sys
import time

IPADD = sys.argv[1]

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ipvoid.com/ip-blacklist-check/")
print(driver.title)

search = driver.find_element_by_name("ip")
search.clear()
search.send_keys(IPADD)
search.send_keys(Keys.ENTER)
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-responsive"))
    )
    print(element.text)
except:
        driver.quit()

driver.quit()