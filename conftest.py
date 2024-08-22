import pytest
from drivers.driver_factory import DriverFactory


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

