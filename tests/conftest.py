import pytest
from selenium import webdriver


# if you want to run on your mentioned browser from command line
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = 'store', default = 'Edge'
    )


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name == 'Edge':
        driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    driver.implicitly_wait(5)
    # return driver  we can't use return when yield is used,So
    request.cls.driver = driver
    yield
    driver.close()
