import pytest, time, os

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session', params=[
    # This will ask your Chrome/Firefox binary version
    # Testing multi-version for a browser needs change browser binary and re-run test.
    ("chrome",  Service(ChromeDriverManager().install())), 
    ("firefox", Service(GeckoDriverManager().install())),
])
def selenium_driver(request):
    browser, browser_driver_service = request.param

    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    driver = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
    }[browser](service=browser_driver_service)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def capture_screenshot_on_test_failed(request):
    yield
    relative_path = str(request.node.path).replace(os.path.abspath(os.path.dirname(__file__)), "").replace(".py", "")
    log_path = f"test_error_log/{relative_path}"
    if not os.path.isdir(log_path):
        os.makedirs(log_path)

    if request.node.rep_setup.failed:
        pass # Setup failed
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            if driver := request.node.funcargs.get("selenium_driver", None):
                take_screenshot(driver, request.node.name, log_path)
            elif user := request.node.funcargs.get("browser_user", None):
                take_screenshot(user.driver, request.node.name, log_path)


def take_screenshot(driver, test_id, log_path):
    time.sleep(1)
    file_name = f'{log_path}/{test_id}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'
    driver.save_screenshot(file_name)