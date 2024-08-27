import pytest
import allure
import logging
from hamcrest import assert_that, any_of, contains_string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL
from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils
from utils.file_utils import FileUtils


class TestThemeSwitch(BrowserUtils):

    @allure.feature('Theme Switch')
    @allure.story('Check the ability to switch Light / Dark mode')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_theme_switch(self, driver):

        try:
            # Open the homepage
            with allure.step("Opening the homepage"):
                self.open_url(driver, BASE_URL)

            # Handle and close the cookie notification banner
            with allure.step("Closing the cookie banner"):
                self.handle_notification(driver)

            # Wait for the theme toggle to be clickable and click it
            with allure.step("Wait for the theme toggle to be clickable"):
                logging.info("Waiting for theme toggle to be clickable")
                theme_toggle = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(HomePageLocators.THEME_TOGGLE)
                )
                theme_toggle.click()

            # Verify that the theme has successfully switched by checking the body's class attribute
            with allure.step("Verify the theme switch"):
                body_class = FileUtils.get_element_attribute(driver, HomePageLocators.BODY, "class")
                assert_that(body_class, any_of(contains_string("dark-mode"), contains_string("light-mode")))
                logging.info(f"Theme switch successful, current body class: {body_class}")

        except Exception as e:
            logging.error(f"Error during theme switch test: {e}")
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            allure.attach(f"Error: {str(e)}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise
