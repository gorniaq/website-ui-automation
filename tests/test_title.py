import logging
import time
import pytest
import allure
from hamcrest import assert_that, equal_to
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config.config import BASE_URL
from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils


class TestMetaTitle(BrowserUtils):

    @allure.feature('Meta Title Check')
    @allure.story('Verify meta title on the homepage')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_meta_title(self, driver):
        """
        Test to verify the meta title on the homepage.
        Raises:
            Exception: Will be raised if an error occurs during the test execution.
        """
        try:
            # Open the homepage
            with allure.step("Opening the homepage"):
                logging.info(f"Opening URL: {BASE_URL}")
                self.open_url(driver, BASE_URL)

            # Wait for the <meta> element with 'og:title' attribute to be present
            with allure.step("Waiting for <meta> element with 'og:title' attribute"):
                meta_title = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(HomePageLocators.META_TITLE)
                )

            # Get the 'content' attribute from the <meta> element
            with allure.step("Getting the 'content' attribute from <meta> element"):
                content = meta_title.get_attribute("content")
                allure.attach(content, name="Meta Title Content", attachment_type=allure.attachment_type.TEXT)

            # Compare the meta title content with the expected value
            with allure.step("Comparing meta title content with expected value"):
                expected_title = "EPAM | Software Engineering & Product Development Services"
                logging.info(f"Expected value: {expected_title}")
                assert_that(content, equal_to(expected_title))
                logging.info("Meta title check passed successfully")

        except Exception as e:
            # Log the error and attach the error details to the allure report
            logging.error(f"Error during meta title check: {e}")
            allure.attach(f"Error: {str(e)}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise e
