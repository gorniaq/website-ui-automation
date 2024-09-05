from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        """
        Create and return a WebDriver instance for the specified browser.
        """
        if browser_name == "chrome":
            # Set up Chrome-specific options
            chrome_options = ChromeOptions()
            # chrome_options.add_argument("--incognito")  # Open Chrome in Incognito mode
            chrome_options.add_argument("--disable-cache")  # Disable caching to ensure fresh data
            chrome_options.add_argument("--window-size=1920,1080")  # Set window size
            chrome_options.add_argument("--headless")  # run Chrome in headless mode
            # Create a Chrome WebDriver instance with the specified options
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        elif browser_name == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--disable-cache")  # Disable caching to ensure fresh data
            # firefox_options.add_argument("--incognito")  # Open Firefox in Private mode
            firefox_options.add_argument("--window-size=1920,1080")  # Set window size
            firefox_options.add_argument("--headless")  # Run Firefox in headless mode
            # Create a Firefox WebDriver instance with the specified options
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        else:
            # Raise an error if an unsupported browser is specified
            raise ValueError(f"Unsupported browser: {browser_name}")

        return driver
