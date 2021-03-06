import pytest, time, os

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# webdriver_manager not support Safari
# webdriver_manager support ChromeDriver, GeckoDriver, IEDriver, OperaDriver, EdgeChromiumDriver
# Need get driver binary by my own...
# See https://pypi.org/project/webdriver-manager/

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage') # overcome limited resource problems
chrome_options.add_argument("--start-maximized")
# chrome_options.binary_location = xxx # 這邊可以指定測試 browser 版本

firefox_options = FirefoxOptions()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox') # Bypass OS security model
firefox_options.add_argument('--disable-dev-shm-usage') # overcome limited resource problems

edge_options = EdgeOptions()
edge_options.add_argument('--headless')
edge_options.add_argument('--no-sandbox') # Bypass OS security model
edge_options.add_argument('--disable-dev-shm-usage') # overcome limited resource problems


@pytest.fixture(scope='session', params=[
    # This will ask your Chrome/Firefox/Edge binary version
    # Testing multi-version for one browser needs to set the browser binary location in option above.
    ("chrome",  ChromeService(ChromeDriverManager().install()), chrome_options), 
    ("firefox", FirefoxService(GeckoDriverManager().install()),  firefox_options),
    ("edge",    EdgeService(EdgeChromiumDriverManager().install()),  edge_options),
])
def selenium_driver(request):
    browser, browser_driver_service, browser_options = request.param

    if browser == "chrome":
         driver = webdriver.Chrome(service=browser_driver_service, options=browser_options)
    elif browser == "firefox":
         driver = webdriver.Firefox(service=browser_driver_service, options=browser_options)
    elif browser == "edge":
         driver = webdriver.Edge(service=browser_driver_service, options=browser_options)
    else:
        raise Exception(f"Unknown browser `{browser}`")
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