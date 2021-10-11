import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException
from selenium.webdriver.common.alert import Alert
driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/Windows.html")

#take the implict wait and take the alert in tab
wait=WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
wait.until(ec.presence_of_element_located((By.NAME, "promtalertb"))).click()
time.sleep(2)

#import alert class

#Create the object for alert class
a_button=Alert(driver)

#using alert class objet call the methods to "1.accept or 2.dismiss or 3.send text and get text " in alert box

time.sleep(2)
text_p=a_button.text
print(text_p)

a_button.send_keys("Code2Lead")

#a_button.accept()
a_button.dismiss()

driver.quit()








