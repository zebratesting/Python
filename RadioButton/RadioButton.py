import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
driver.maximize_window()

time.sleep(2)

#finding the list of radio buttons using locatior

ele_r=driver.find_elements(By.NAME,'radio')
time.sleep(2)


#Using for loop for getting Radio buttons

for rbutton in ele_r:
    rbutton_t=rbutton.get_attribute("value")
    print(rbutton_t)
    if rbutton_t=="Button4":
        rbutton.click()
        print("is_selected",rbutton.is_selected())
        break



time.sleep(2)
driver.quit()