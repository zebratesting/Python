import time

from selenium import webdriver

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
driver.maximize_window()

driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@name="textbox"]').send_keys("Sample")

time.sleep(5)
driver.quit()


