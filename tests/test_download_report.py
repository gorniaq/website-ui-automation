import allure
from hamcrest import assert_that, is_

from locators.about_page_locators import AboutPageLocators
from utils.browser_utils import BrowserUtils
from utils.file_utils import FileUtils
from config.config import ABOUT_URL
from constants import EXPECTED_FILE_NAME


class TestDownloadReport(BrowserUtils):

    @allure.feature('Report Download Check')
    @allure.story('Verify report download functionality')
    def test_download_report(self, driver):
        """
        Test to verify that the report can be downloaded successfully.
        """
        # Open the homepage and close the cookie notification banner
        self.open_url_and_handle_notification(driver, ABOUT_URL)

        # Scroll to the report download section on the page
        with allure.step("Scroll to the report download section"):
            self.scroll_to_element(driver, AboutPageLocators.REPORT_DOWNLOAD_SECTION)

        # Wait for the download button to be clickable, then click it
        with (allure.step("Wait for the download button to be clickable")):
            self.wait_for_element_and_click(driver, AboutPageLocators.DOWNLOAD_BUTTON, 30)

        # Verify that the report has been downloaded
        with allure.step("Verify that the report is downloaded"):
            file_found = FileUtils.verify_file_download(EXPECTED_FILE_NAME)
            # Assert that the file was found in the download directory
            assert_that(file_found, is_(True),
                        f"Expected file '{EXPECTED_FILE_NAME}' not found in download directory")
