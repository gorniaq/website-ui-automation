import pytest
import allure
import logging
from hamcrest import assert_that, equal_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import ABOUT_URL, BASE_URL
from locators.about_page_locators import AboutPageLocators
from utils.browser_utils import BrowserUtils


class TestLogoRedirectsToHomepage(BrowserUtils):
    @allure.feature("Navigation Functionality")
    @allure.story("Verify that clicking the company logo redirects to the homepage")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_logo_redirects_to_homepage(self, driver):
        """
            Test case to verify that clicking the company logo redirects to the homepage.
            Raises:
                Exception: If any error occurs during the test.
        """
        try:
            with allure.step("Open URL and close the cookie banner"):
                # Open the ABOUT page URL and handle any cookie banners or notifications.
                self.open_url(driver, ABOUT_URL)
                self.handle_notification(driver)

            with allure.step("Waiting for the company logo to be clickable"):
                #  Wait for the company logo to be clickable.
                logo = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(AboutPageLocators.COMPANY_LOGO_LINK)
                )
                logging.info("Company logo is now clickable.")

            with allure.step("Clicking the company logo"):
                # Click the company logo.
                logo.click()
                logging.info("Company logo clicked.")

            with allure.step("Verifying the redirect to the homepage"):
                # Verify that the current URL is the homepage URL.
                current_url = driver.current_url
                allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
                assert_that(current_url, equal_to(BASE_URL))
                logging.info(f"Successfully redirected to: {current_url}")

        except Exception as e:
            logging.error(f"Error during company logo redirect check: {e}")
            allure.attach(f"Error: {str(e)}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise
