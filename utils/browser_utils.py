import logging
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger_config import logger
from locators.home_page_locators import HomePageLocators


class BrowserUtils:
    @staticmethod
    def open_url_and_handle_notification(driver, url, expected_url=None):
        """Opens a URL in the browser, handles any notifications, and optionally verifies that the correct URL is loaded.
        Args:
            driver (WebDriver): The WebDriver instance.
            url (str): The URL to open.
            expected_url (str, optional): The URL to verify after loading. Defaults to None.
        """
        logging.info(f"Opening URL: {url}")
        driver.get(url)

        # Handle notification (e.g., cookie banner)
        BrowserUtils.handle_notification(driver)

        # If an expected URL is provided, verify it matches the current URL
        if expected_url:
            WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))

    @staticmethod
    def wait_for_element(driver, locator, timeout=20):
        """Waits for an element to be present in the DOM and returns it.
        Args:
            driver (WebDriver): The WebDriver instance.
            locator (tuple): The locator of the element, e.g., (By.ID, 'element_id').
            timeout (int, optional): Maximum time to wait for the element. Defaults to 20 seconds.
        Returns:
            WebElement: The located element.
        """
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @staticmethod
    def wait_for_element_to_be_clickable(driver, locator, timeout=20):
        """
        Wait for an element to be clickable.
        Args:
            driver (WebDriver): The WebDriver instance.
            locator (tuple): The locator of the element to wait for.
            timeout (int): The maximum time to wait for the element to be clickable.
        Returns:
            WebElement: The element once it is clickable.
        """
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def get_element_attribute(driver, locator, attribute):
        """
        Retrieves the value of a specified attribute from an element located by the provided locator.
        Args:
            driver (webdriver): The WebDriver instance used to interact with the browser.
            locator (tuple): A tuple containing the locator strategy and value to locate the element.
            attribute (str): The name of the attribute whose value is to be retrieved.
        Returns:
            str: The value of the specified attribute from the located element.
        """
        # Use wait_for_element to wait until the element is present in the DOM
        element = BrowserUtils.wait_for_element(driver, locator, timeout=20)
        # Retrieve and return the value of the specified attribute from the located element
        return element.get_attribute(attribute)

    @staticmethod
    def get_element_text(driver, locator):
        """
        Retrieves the text content from an element located by the provided locator.
        Args:
            driver (webdriver): The WebDriver instance used to interact with the browser.
            locator (tuple): A tuple containing the locator strategy and value to locate the element.
        Returns:
            str: The text content of the located element.
        """
        # Use wait_for_element to wait until the element is present in the DOM
        element = BrowserUtils.wait_for_element(driver, locator, timeout=20)
        # Retrieve and return the text content from the located element
        return element.text

    @staticmethod
    def verify_url(driver, expected_url, timeout=20):
        """
        Verifies that the current URL matches the expected URL.
        Args:
            driver (WebDriver): The WebDriver instance.
            expected_url (str): The URL that is expected to be loaded.
            timeout (int, optional): Maximum time to wait for the URL to match. Defaults to 20 seconds.
        """
        WebDriverWait(driver, timeout).until(
            EC.url_to_be(expected_url)
        )
        logging.info(f"URL verified: {expected_url}")

    @staticmethod
    def scroll_to_element(driver, locator):
        """Scrolls the page until the specified element is in view.
        Args:
            driver (WebDriver): The WebDriver instance.
            locator (tuple): The locator of the element to scroll to, e.g., (By.ID, 'element_id').
        """
        element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(locator)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.info(f"Scrolled to element with locator: {locator}")

    @staticmethod
    def scroll_to_top(driver):
        """Scrolls to the top of the page.
        Args:
            driver (WebDriver): The WebDriver instance.
        """
        driver.execute_script("window.scrollTo(0, 0);")
        logger.info("Scrolled to the top of the page")

    @staticmethod
    def _wait_for_notification_to_disappear(driver, timeout=30):
        """
        Wait for the cookies notification to disappear from the page.
        Args:
            driver: The WebDriver instance used to interact with the browser.
            timeout: Maximum time (in seconds) to wait for the notification to disappear.
        """
        try:
            # Wait until the notification is no longer visible on the page
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located(HomePageLocators.COOKIE_BANNER)
            )
            logger.info("Notification has disappeared.")
        except TimeoutException:
            # Log a warning if the notification did not disappear within the given timeout
            logger.warning("Notification did not disappear within the given timeout.")

    @staticmethod
    def _close_notification(driver):
        """
        Close the notification if it is present.
        Args:
            driver: The WebDriver instance used to interact with the browser.
        """
        try:
            # Wait until the notification close button is clickable
            close_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(HomePageLocators.COOKIE_ACCEPT_BUTTON)
            )
            BrowserUtils.scroll_to_element(driver, HomePageLocators.COOKIE_ACCEPT_BUTTON)
            close_button.click()  # Click the close button to close the notification
            logger.info("Notification was closed.")

        except TimeoutException:
            # Log info if the notification close button was not present or clickable
            logger.info("Notification close button was not present or clickable.")

    @staticmethod
    def handle_notification(driver):
        """
        Handle the notification: close it if present, or wait for it to disappear.
        Args:
            driver: The WebDriver instance used to interact with the browser.
        """
        # Attempt to close the notification
        BrowserUtils._close_notification(driver)
        # Wait for the notification to disappear if it was not closed
        BrowserUtils._wait_for_notification_to_disappear(driver)
