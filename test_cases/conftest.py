import pytest
import undetected_chromedriver as uc
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser : chrome or firefox or edge")

# browser fixture
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# setup fixture
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = uc.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    yield driver
    driver.quit()


###########for pytest html reports ###########
#hook for adding environment info in html report
def pytest_configure(config):
   config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, nopcommerce'
   config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
   config.stash[metadata_key]['Tester Name'] = 'Swetha'

#hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
   metadata.pop('JAVA_HOME',None)
   metadata.pop('Plugins', None)



