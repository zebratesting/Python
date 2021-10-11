import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
driver.maximize_window()

time.sleep(2)

#finding the list of check box using locatior

ele_r=driver.find_elements(By.NAME,'checkbox')
time.sleep(2)


#Using for loop for getting Radio buttons

for CheckBoxes in ele_r:
    rbutton_t=CheckBoxes.get_attribute("value")
    print(rbutton_t)
    if rbutton_t=="c3":
        CheckBoxes.click()
        print("is_selected",CheckBoxes.is_selected())
        break



time.sleep(2)
driver.quit()