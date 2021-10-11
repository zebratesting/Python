import time

from SeleniumFrameWork.Base.DriverClass import WebDriverClass
import SeleniumFrameWork.Utilities.CustomLogger as cl
from SeleniumFrameWork.Base.BasePage import  BaseClass


wd=WebDriverClass()

driver=wd.getWebDriver("firefox")
bp=BaseClass(driver)
bp.launchWedPage("http://www.dummypoint.com/seleniumtemplate.html","Selenium Template — DummyPoint")
ele=bp.getWebElement("user_input","id")
ele.send_keys("Selenium")

time.sleep(2)
driver.quit()

