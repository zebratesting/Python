import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
driver.maximize_window()
time.sleep(2)


wait=WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
ele=wait.until(ec.presence_of_element_located((By.ID,"multiselect")))


#import the select class

#Create object for select class
ms_options=Select(ele)

print("Check whether it is a multiselect or not: ",ms_options.is_multiple)

#List the values in multi select

ms_v=ms_options.options
for ms_value in ms_v:
    print(ms_value.text)

#click by index
ms_options.select_by_index(1)

#Click by value
ms_options.select_by_value("mOptionThree")

#click by text
ms_options.select_by_visible_text("mOption4")


# deselect_by_index
ms_options.deselect_by_index(1)
time.sleep(2)

# deselect_by_value
ms_options.deselect_by_value("mOptionTWo")
time.sleep(2)

# deselect_by_visible_text
ms_options.deselect_by_visible_text("mOption3")
time.sleep(2)


# Click by Index
ms_options.select_by_index(1)
# Click by Value
ms_options.select_by_value("mOptionTWo")
# Click by Text
ms_options.select_by_visible_text("mOption3")

time.sleep(2)

# deselect_all
ms_options.deselect_all()

time.sleep(5)
driver.quit()

