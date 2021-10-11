from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

def amazonPage():
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    title=driver.title
    print("Page title is ",title)
    driver.find_element_by_xpath("//div[@id='nav-xshop-container']/div/a[2]").click()
    title2=driver.title
    print("Page title is:",title2)
    driver.back()
    tit=driver.title
    if tit==title:
        print("Navigated back to homepage",tit)

    driver.close()

amazonPage()

