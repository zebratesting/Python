import time

from selenium import webdriver

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
driver.maximize_window()
time.sleep(2)

driver.get('http://www.dummypoint.com/Form.html')
time.sleep(10)

driver.back()
time.sleep(10)
print(driver.title)
driver.refresh()
driver.forward()
time.sleep(2)
print(driver.title)
assert "Form 1"
time.sleep(2)
driver.quit()


