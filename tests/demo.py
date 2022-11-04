from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Browser
# service_obj = Service("C://Users//sweth//OneDrive//Desktop//webdrivers//chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# Added comment

# Firefox Browser
# service_obj = Service("C://Users//sweth//OneDrive//Desktop//webdrivers//geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

# Edge Browser
def test_first(self):
    service_obj = Service ( "C://Users//sweth//OneDrive//Desktop//webdrivers//msedgedriver.exe" )
    driver = webdriver.Edge ( service=service_obj )
    driver.get ( "https://smartconnect-dev-us.telrock.com/portal/login/qa/man" )
    print ( driver.title )
    print ( driver.current_url )
    driver.close ()
