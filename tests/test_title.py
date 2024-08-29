import pytest
import allure
from hamcrest import assert_that, equal_to
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
        """
        # Open the homepage and close the cookie notification banner
        with allure.step("Open URL and close the cookie banner"):
            self.open_url_and_handle_notification(driver, BASE_URL)

        # Wait for the <meta> element with 'og:title' attribute to be present
        with allure.step("Waiting for <meta> element with 'og:title' attribute"):
            meta_title = self.wait_for_element(driver, HomePageLocators.META_TITLE, 20)

        # Get the 'content' attribute from the <meta> element
        with allure.step("Getting the 'content' attribute from <meta> element"):
            content = meta_title.get_attribute("content").strip()

        # Compare the meta title content with the expected value
        with allure.step("Comparing meta title content with expected value"):
            expected_title = "EPAM | Software Engineering & Product Development Services"
            assert_that(content, equal_to(expected_title),
                        f"Meta title does not match: expected '{expected_title}', but got '{content}'")
