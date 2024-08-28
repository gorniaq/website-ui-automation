import pytest
import allure
from hamcrest import assert_that, equal_to

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
        """
        # Open the homepage and close the cookie notification banner
        with allure.step("Open URL and close the cookie banner"):
            self.open_url_and_handle_notification(driver, ABOUT_URL)

        #  Wait for the company logo to be clickable.
        with allure.step("Waiting for the company logo to be clickable and click"):
            logo = self.wait_for_element(driver, AboutPageLocators.COMPANY_LOGO_LINK, 20)
            logo.click()

        # Verify that the current URL is the homepage URL.
        with allure.step("Verifying the redirect to the homepage"):
            current_url = driver.current_url
            assert_that(current_url, equal_to(BASE_URL))
