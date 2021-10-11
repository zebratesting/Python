import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

driver.get("https://www.goibibo.com/")
driver.maximize_window()

assert "Goibibo - Best Travel Website. Book Hotels, Flights, Trains, Bus and Cabs with upto 50% off" in driver.title
driver.find_element_by_xpath("//div[@class='dF justifyCenter padTB20 fltSwitchOpt-wrp']/div/span[1]").is_selected()
time.sleep(2)
depart_from=driver.find_element(By.XPATH,'//input[@placeholder="From"]')
depart_from.click()
time.sleep(2)
depart_from.send_keys("New Delhi")
time.sleep(2)
depart_from.send_keys(Keys.ARROW_DOWN)
depart_from.send_keys(Keys.ENTER)
time.sleep(2)
going_to=driver.find_element(By.XPATH,"//input[@placeholder='Destination']")
going_to.send_keys("Canada")
time.sleep(5)
going_to.send_keys(Keys.ARROW_DOWN)
going_to.send_keys(Keys.ENTER)

#Date Selection
time.sleep(2)
driver.find_element(By.ID,"departureCalendar").click()
time.sleep(2)
Month_Displayed=driver.find_element(By.XPATH,"//div[@class='DayPicker-NavBar']/span[2]").click()
driver.find_element(By.ID,"fare_20210909").click()

driver.find_element(By.ID,"defence_fare_check").click()







time.sleep(5)

driver.quit()