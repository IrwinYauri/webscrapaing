from selenium import webdriver

DRIVER_PATH = 'D:\EDUCO\webscrapaing\scrapingSelenium\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')