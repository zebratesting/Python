import time

from selenium import webdriver

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")


assert "Selenium Template"  in driver.title
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(2)
print(driver.current_url)
driver.quit()