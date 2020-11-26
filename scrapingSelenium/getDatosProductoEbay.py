from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path='D:\EDUCO\github\webscrapaing\scrapingSelenium\chromedriver.exe')
driver.get("https://www.ebay.com/itm/Dyson-V7-Fluffy-HEPA-Cordless-Vacuum-Cleaner-Blue-New/273976851242")

title = driver.find_element_by_xpath('//h1')
current_price = driver.find_element_by_xpath("//span[@id='prcIsum']")
image = driver.find_element_by_xpath("//img[@id='icImg']")

product_data = {
	'title': title.text,
	'current_price': current_price.get_attribute('content'), 
	'image_url': image.get_attribute('src')
}

print(product_data)
driver.quit()