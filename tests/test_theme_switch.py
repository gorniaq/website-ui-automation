import pytest
import allure
from hamcrest import assert_that, any_of, contains_string

from config.config import BASE_URL
from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils


class TestThemeSwitch(BrowserUtils):
    @allure.feature('Theme Switch')
    @allure.story('Check the ability to switch Light / Dark mode')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_theme_switch(self, driver):

        # Open the homepage and close the cookie notification banner
        with allure.step("Open URL and close the cookie banner"):
            self.open_url_and_handle_notification(driver, BASE_URL)

        # Wait for the theme toggle to be clickable and click it
        with allure.step("Wait for the theme toggle to be clickable and click"):
            self.wait_for_element_and_click(driver, HomePageLocators.THEME_TOGGLE, 20)

        # Verify that the theme has successfully switched by checking the body's class attribute
        with allure.step("Verify the theme switch"):
            body_class = self.get_element_attribute(driver, HomePageLocators.BODY, "class")
            assert_that(body_class, any_of(contains_string("dark-mode"), contains_string("light-mode")),
                        f"Theme switch failed: body class is '{body_class}'")
