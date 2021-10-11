import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/Windows.html")

wait=WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

wait.until(ec.presence_of_element_located((By.NAME,"alertbutton"))).click()
#import alert
alert_a=Alert(driver)
time.sleep(2)

text_a=alert_a.text
print(text_a)

alert_a.accept()

driver.quit()
