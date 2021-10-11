import time

from selenium import webdriver

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("https://www.google.com/")
time.sleep(5)
driver.quit()

