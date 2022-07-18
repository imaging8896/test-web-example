import pytest, time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session', params=[
    ("chrome", Service(ChromeDriverManager().install())),
])
def selenium_driver(request):
    browser, browser_driver_service = request.param

    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    driver = {
        "chrome": webdriver.Chrome
    }[browser](service=browser_driver_service)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def capture_screenshot_on_test_failed(request):
    yield
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            if driver := request.node.funcargs.get("selenium_driver", None):
                take_screenshot(driver, request.node.nodeid)
            elif user := request.node.funcargs.get("browser_user", None):
                take_screenshot(user.driver, request.node.nodeid)

            print("executing test failed", request.node.nodeid)


def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/","_").replace("::","__")
    driver.save_screenshot(file_name)