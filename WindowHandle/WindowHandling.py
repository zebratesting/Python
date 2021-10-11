import time

from selenium.common.exceptions import ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/Windows.html")
assert "Selenium Template" in driver.title
time.sleep(2)

#add wait element to create explicit wait to script

wait=WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

#To get the current window name
Window_Name=driver.current_window_handle
print("Before switching",Window_Name)
time.sleep(2)
#Click on the pop up button to open the new window
ele=driver.find_elements(By.TAG_NAME,"input")
for popup_bt in ele:
    popup=popup_bt.get_attribute("value")
    if popup=="Open a Popup Window2":
        popup_bt.click()
#Print the list of winows in screen in present seddion
Windows=driver.window_handles
for window in Windows:
    print(window)
#switch to required window
driver.switch_to.window(Windows[1])
time.sleep(2)
window_name=driver.current_window_handle
print("After switching",window_name)
driver.maximize_window()

#Here Switching to new window and performing action on frame
time.sleep(2)
ele=driver.find_element(By.ID,"f2")
driver.switch_to.frame(ele)


data=driver.find_element(By.ID,"framename")
print("Framename:",data.text)
time.sleep(2)
#Close Browser
driver.quit()

