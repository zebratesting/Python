from behave import *
from selenium import webdriver

@given('launch firefox browser')
def LaunchBrowser(context):
    context.driver = webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")



@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get('https://www.orangehrm.com/')



@then('verify that the logo present on page')
def VerifyLogoPage(context):
    status=context.driver.find_element_by_xpath('/html/body/nav/div/div[1]/a/img').is_displayed()
    assert status is True

@then('close browser')
def step_impl(context):
    context.driver.close()
