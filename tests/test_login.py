import pytest
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class Login(BaseClass):
    def test_login(self):
        print("test_login")
        self.driver.find_element(By.XPATH("/html/body/app-root/app-login/div/div/button/span")).click()
