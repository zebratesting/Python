import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

#to see the code for impoerted methods click on ctrl

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
driver.maximize_window()
time.sleep(2)


wait=WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
ele=wait.until(ec.presence_of_element_located((By.ID,"dropdown")))

#import select class

#create the object for select class
dd_options=Select(ele)

#List the values in drop down
dd_v=dd_options.options
for dd_values in dd_v:
    print(dd_values.text)

#click by index
dd_options.select_by_index(2)
time.sleep(2)

#click by value
dd_options.select_by_value("OptionThree")
time.sleep(2)

#click by text
dd_options.select_by_visible_text("Option5")

time.sleep(5)
driver.quit()

