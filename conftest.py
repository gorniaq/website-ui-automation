import pytest
from drivers.driver_factory import DriverFactory
import allure


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture for initializing and managing the WebDriver instance.
    The fixture's scope is set to "function", meaning a new WebDriver instance
    will be created for each test function. The WebDriver instance is initialized
    based on the browser specified in the command-line options. After the test
    function completes, the WebDriver instance is closed.
    Returns:
        WebDriver: The initialized WebDriver instance.
    """
    # Retrieve the browser name from the pytest parameterization to initialize the appropriate WebDriver
    browser_name = request.param

    # Initialize the WebDriver for the specified browser
    driver = DriverFactory.get_driver(browser_name)

    # Provide the WebDriver instance to the test function
    yield driver
    driver.quit()


def pytest_generate_tests(metafunc):
    """
    This hook will be invoked for every test case, and it will parameterize
    the 'driver' argument to use both 'chrome' and 'firefox'.
    """
    if "driver" in metafunc.fixturenames:
        # Define the browser types (chrome, firefox) you want to test
        browsers = ["chrome", "firefox"]

        # Set the parameterization for the 'driver' argument
        metafunc.parametrize("driver", browsers, indirect=True)




@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach a screenshot and error details to the Allure report if a test fails.
    """
    outcome = yield
    report = outcome.get_result()

    # We only want to take a screenshot for the final call of the test, not setup or teardown
    if report.when == 'call' and report.failed:
        # Get the WebDriver instance from the test item
        driver = item.funcargs.get('driver')
        if driver is not None:
            # Take a screenshot and attach it to the Allure report
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

        # Attach the error text to the Allure report
        error_message = str(report.longrepr)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
