from selenium import webdriver

driver=webdriver.Firefox(executable_path="/work/Drivers/drivers/geckodriver.exe")

def url():
    driver.get("https://in.godaddy.com/")
    driver.maximize_window()
    ele=driver.title
    print(f'"{ele}" is the title of page')
    url=driver.current_url
    print(f'Current url is "{url}"')
    page_source=driver.page_source
    print(f'{page_source} \n page source')
    assert "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy IN" in driver.title
    driver.close()

url()
