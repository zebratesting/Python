import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
driver.maximize_window()

assert "Selenium Template" in driver.title

time.sleep(2)

wait=WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
wait.until(ec.presence_of_element_located((By.LINK_TEXT,"Form"))).click()
wait.until(ec.presence_of_element_located((By.ID,"reused_form")))
time.sleep(2)

wait.until(ec.presence_of_element_located((By.XPATH,"//*[@id='reused_form']/div[1]/input"))).send_keys("Demo")
wait.until(ec.presence_of_element_located((By.XPATH,"//*[@id='reused_form']/div[2]/input"))).send_keys("a.g@gmail.com")
wait.until(ec.presence_of_element_located((By.XPATH,"//*[@id='g'][2]"))).click()
wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="reused_form"]/div[4]/input'))).send_keys("Tech")
wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="reused_form"]/div[5]/textarea'))).send_keys("Demo message")

captcha = wait.until(ec.presence_of_element_located((By.ID,"captcha_image")))
wait.until(ec.presence_of_element_located((By.ID,"captcha"))).send_keys(captcha.text)

postButton = wait.until(ec.presence_of_element_located((By.ID,"btnContactUs")))

actions=ActionChains(driver)
actions.move_to_element(postButton).perform()
postButton.click()
time.sleep(5)
driver.quit()

