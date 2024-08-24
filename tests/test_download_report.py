import pytest
import allure
import logging
import os
import time

from hamcrest import assert_that, is_
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.about_page_locators import AboutPageLocators
from utils.browser_utils import BrowserUtils
from utils.file_utils import FileUtils
from config.config import ABOUT_URL, EXPECTED_FILE_NAME


class TestDownloadReport(BrowserUtils):
    @staticmethod
    def verify_file_download(expected_file_name):
        """
        Verify that the expected file has been downloaded to the default download directory.
        Args:
            expected_file_name (str): The name of the file expected to be downloaded.
        Raises:
            AssertionError: If the expected file is not found within the timeout period.
        """
        file_found = False
        # Record the start time of the verification
        start_time = time.time()
        # Get the path to the download directory
        download_dir = FileUtils.get_download_dir()

        # Wait up to 60 seconds for the file to appear in the download directory
        while time.time() - start_time < 60:
            # List all files in the download directory
            files = os.listdir(download_dir)
            for file in files:
                # Check if there is a file with a .pdf extension and the expected file name
                if file.endswith(".pdf") and expected_file_name in file:
                    logging.info(f"Downloaded file found: {file}")
                    file_found = True
                    break
            if file_found:
                break

        return file_found

    @allure.feature('Report Download Check')
    @allure.story('Verify report download functionality')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_download_report(self, driver):
        """
        Test to verify that the report can be downloaded successfully.
        """
        try:
            # Open the URL and close the cookie banner
            with allure.step("Open URL and close the cookie banner"):
                self.open_url(driver, ABOUT_URL)
                # Close cookie banner
                self.handle_notification(driver)

            # Scroll to the report download section on the page
            with allure.step("Scroll to the report download section"):
                self.scroll_to_element(driver, AboutPageLocators.REPORT_DOWNLOAD_SECTION)
                logging.info("Scrolled to the report download section")

            # Wait for the download button to be clickable, then click it
            with allure.step("Wait for the download button to be clickable"):
                download_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable(AboutPageLocators.DOWNLOAD_BUTTON)
                )
                download_button.click()
                logging.info("Clicked the download button for the report")

            # Verify that the report has been downloaded
            with allure.step("Verify that the report is downloaded"):
                file_found = self.verify_file_download(EXPECTED_FILE_NAME)
                # Assert that the file was found in the download directory
                assert_that(file_found, is_(True),
                            f"Expected file '{EXPECTED_FILE_NAME}' not found in download directory")

        except Exception as e:
            logging.error(f"Error during file download check: {e}")
            allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(f"Error: {e}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise
