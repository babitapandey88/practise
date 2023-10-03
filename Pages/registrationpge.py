from selenium.webdriver.common.by import By

from Library import configreder

class registion:

    def __init__(self,obj):
        global driver
        driver=obj
    def enterusername(self,username):
     driver.find_element(By.NAME, configreder.fetchelemnt("Registration", "username_name")).send_keys(username)
    def passw(self,password):
     driver.find_element(By.NAME, configreder.fetchelemnt("Registration", "password_name")).send_keys(password)
    def emil(self,email):
     driver.find_element(By.NAME, configreder.fetchelemnt("Registration", "email_name")).send_keys(email)



