from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'D:\EDUCO\github\webscrapaing\scrapingSelenium\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get("https://cuantic.000webhostapp.com/vista/login.php")

login = driver.find_element_by_xpath("//input[@type='text']").send_keys('40506070')
#password = driver.find_element_by_xpath("//input[@type='password']").send_keys('1234567gdf9')
#submit = driver.find_element_by_xpath("//input[@value='login']").click()
driver.execute_script("ejecutar();")
try:
    logout_button = driver.find_element_by_id("export_data")
    print('Successfully logged in')
    try:
        element = WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.ID, "export_data"))#captura de pantalla           
        )
    finally:
        #driver.quit()
        driver.save_screenshot('screenshot.png')
    
except NoSuchElementException:
    print('Incorrect login/password')