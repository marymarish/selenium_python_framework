import os.path
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

from utilities.readProperties import ReadConfig


# scope="function" for each test case
# scope="session" for all file
# by default scope = function.
# class because we want to apply to class in test_login
# there are also autouse=True to aply automatically to every TC

@pytest.fixture(scope="class")
def setup(request, browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    # elif browser == "opera":
    #     driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        print("Provide valid browser")
    # driver.get(ReadConfig.getApplicationURL())
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    #parser.addoption("--url")

# second. methods for each browser:
@pytest.fixture(scope="class", autouse=True)
def browser(request):  # return the browser value to setup method
    return request.config.getoption("--browser")

# @pytest.fixture(scope="class", autouse=True)
# def url(request):  # return the browser value to setup method
#     return request.config.getoption("--url")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    global html
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://www.jetblue.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_diirectory = os.path.dirname(item.config.option.htmlpath)
            # random_name:
            #file_name = str(int(round(time.time() * 1000))) + ".png"
            # file name as test name:
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_diirectory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img> src="%s" alt="screenshot" style="width:300px;height=200px"' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra

# automatically change report name:
def pytest_html_report_title(report):
    report.title = "Airline Automatiton Report"