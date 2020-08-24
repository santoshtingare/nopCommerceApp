from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser== 'chrome':
       driver = webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver.exe")
       driver.maximize_window()
       driver.implicitly_wait(6)
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/Santosh/Desktop/FirefoxDriver/geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(6)

    return driver

def pytest_addoption(parser):  # This will get the value from the command line
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return browser value to setup method
    return request.config.getoption("--browser")


################# PyTest HTML Report ############################
# It is hook for Adding Environment info to HTML report

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Santosh'

# It is hook for delete/Modify Environment info to HTML Report
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
 #   metadata.pop("JAVA_HOME", None)
  #  metadata.pop("Plugins", None)