import pytest

# @pytest.yield_fixture(scope='session')
# def browser():
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

from selenium import webdriver
import pytest
driver = None

'''
def pytest_runtest_setup(item):
    print
    print("\n######################\n setting up\n######################\n", item)
'''

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="file:/D:/Selenium_firefox/cvescanauto/resultreport/%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file("D:\\Selenium_firefox\\cvescanauto\\resultreport\\"+name)
    #    D:\\Selenium_firefox\\cvescanauto\\resultreport\\
    # driver.get_screenshot_as_file(name)


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()
    #driver.close()
    return driver

pytest
