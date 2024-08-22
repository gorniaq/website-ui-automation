import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class FileUtils:

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
        # Wait until the element is visible on the page
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        # Retrieve the value of the specified attribute from the located element
        attribute_value = element.get_attribute(attribute)
        return attribute_value

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
        # Wait until the element is visible on the page
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        # Retrieve the text content from the located element
        element_text = element.text
        return element_text

    @staticmethod
    def get_download_dir():
        if os.name == 'nt':  # Windows
            return os.path.expanduser('~\\Downloads')
        else:  # Linux, macOS
            return os.path.expanduser('~/Downloads')