import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get('https://www.techlistic.com/')
driver.maximize_window()


ele =driver.find_elements(By.XPATH,"//li[@class='overflowable-item']")

for e in ele:

    if e.text=="SELENIUM":
        time.sleep(2)
        driver.find_element_by_xpath("//li[@class='overflowable-item'][1]").click()
        time.sleep(2)
        print(driver.title)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        print(driver.title)
        break


ele =driver.find_elements(By.XPATH,"//li[@class='overflowable-item']")

for e in ele:

    if e.text=="BLOGS":
        #return self._execute(Command.GET_ELEMENT_TEXT)['value']
        driver.find_element_by_xpath("//li[@class='overflowable-item'][8]").click()
        time.sleep(2)
        print(driver.title)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        print(driver.title)
        time.sleep(5)
        break
ele =driver.find_elements(By.XPATH,"//li[@class='overflowable-item']")

for e in ele:

    if e.text=="JAVA":
        #return self._execute(Command.GET_ELEMENT_TEXT)['value']
        driver.find_element_by_xpath("//li[@class='overflowable-item'][3]").click()
        time.sleep(2)
        print(driver.title)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        print(driver.title)
        time.sleep(5)
        break

driver.close()