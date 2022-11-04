import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.service import Service


@pytest.fixture(scope="class")
def setup(request):
    print("conftest")
    service_obj = Service("C://Users//sweth//OneDrive//Desktop//webdrivers//chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://smartconnect-dev-us.telrock.com/portal/login/qa/man")
    print(driver.title)
    print(driver.current_url)
    request.cls.driver = driver
    yield
    driver.close()