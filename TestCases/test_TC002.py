from selenium.webdriver.common.by import By
from Library import configreder

from Base import initiateDruver
from Pages import registrationpge


def test_invalid():
    driver = initiateDruver.start_br()
    regis = registrationpge.registion(driver)
    regis.passw("jhdc")