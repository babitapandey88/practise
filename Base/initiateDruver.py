from selenium.webdriver import Chrome
from Library import configreder
from selenium.webdriver import Firefox

def start_br():
    global driver
    if((configreder.readConfigdata('Details','Browser'))=="Chrome"):
     path = "C:\\Users\\Dell\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe"
     driver = Chrome()
    elif((configreder.readConfigdata('Details','Browser'))=="firefox"):
     driver =Firefox()
    else:
        path = "C:\\Users\\Dell\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe"
        driver = Chrome()
    driver.get(configreder.readConfigdata('Details','Application_URL'))
    driver.maximize_window()
    return driver

def close():
    driver.close()