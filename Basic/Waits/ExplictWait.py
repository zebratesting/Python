import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
driver.maximize_window()
time.sleep(2)
wait=WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

ele=wait.until(ec.presence_of_element_located((By.ID,"user_input")))

driver.find_element_by_xpath('//*[@name="textbox"]').send_keys("Sample")

time.sleep(5)
driver.quit()

