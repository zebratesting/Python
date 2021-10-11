import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/Frame.html")
driver.maximize_window()
time.sleep(2)


assert "Selenium Template" in driver.title


wait=WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele=driver.find_elements(By.TAG_NAME, "iframe")

#Get the number of frames
print("List the no of Frames:",len(ele))

"""
#Switch to frame by index
driver.switch_to.frame(0)
dis=driver.find_element_by_id("framename")
print("Display the text from frame",dis.text)
"""

"""
#Switch to frame by name
time.sleep(2)
driver.switch_to.frame("farme2")
dis=driver.find_element_by_id("framename")
print("Display the text from frame",dis.text)
"""

#Switch to frame by id
time.sleep(2)
driver.switch_to.frame("f4")
dis=driver.find_element_by_id("framename")
print("Display the text from frame",dis.text)

"""
# Switch to iframe by WebElement

time.sleep(2)
ele = driver.find_element(By.ID,"f2")
driver.switch_to.frame(ele)
"""

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)


# Switching back to normal content page from frame
time.sleep(2)
driver.switch_to.default_content()

data = driver.find_element(By.ID,"framename")
print("Webpage Name is : ",data.text)

time.sleep(2)
driver.quit()







time.sleep(2)
driver.quit()




