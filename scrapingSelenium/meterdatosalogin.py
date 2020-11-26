from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'D:\EDUCO\github\webscrapaing\scrapingSelenium\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get("https://news.ycombinator.com/login")

login = driver.find_element_by_xpath("//input").send_keys('irwin123456')
password = driver.find_element_by_xpath("//input[@type='password']").send_keys('1234567gdf9')
submit = driver.find_element_by_xpath("//input[@value='login']").click()

try:
    logout_button = driver.find_element_by_id("logout")
    print('Successfully logged in')
except NoSuchElementException:
    print('Incorrect login/password')
    
