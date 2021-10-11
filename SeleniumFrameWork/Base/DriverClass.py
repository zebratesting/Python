from selenium import webdriver
import SeleniumFrameWork.Utilities.CustomLogger as cl

class WebDriverClass:
    log=cl.customLogger()
    def getWebDriver(self,browserName):
        driver = None
        if browserName == "firefox":
            driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")
            self.log.info("Firefox browser is initialising")
        elif browserName=="safari":
            driver=webdriver.Safari()
            self.log.info("Firefox browser is initialising")
        return driver

