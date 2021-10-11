from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")


driver.get("https://www.amazon.in/")

ele=driver.find_elements(By.XPATH,"//div[@id='nav-xshop-container']/div/a")

for e in ele:
    print(e.text)
