# conftest.py
import pytest
from selenium import webdriver

# Handling irritating ads on the test site by blocking and rerouting them to my own pc 
# Ad servers are redirected to your own computer, so ads never load
AD_BLOCK_RULES = ", ".join(
    f"MAP {domain} 127.0.0.1"
    for domain in [
        "googleads.g.doubleclick.net",
        "pagead2.googlesyndication.com",
        "tpc.googlesyndication.com",
        "www.googletagservices.com",
    ]
)


def pytest_addoption(parser):
    parser.addoption("--browser", 
    action="store", 
    default="chrome",
    help="Browser to run tests on: chrome or firefox")
    
    parser.addoption("--headless", 
    action="store_true",
    help="Run browser without opening a window")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument(f"--host-resolver-rules={AD_BLOCK_RULES}")
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()