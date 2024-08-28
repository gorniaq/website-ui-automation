import pytest
import allure
from hamcrest import assert_that, contains_string, equal_to

from config.config import BASE_URL, UA_WEBSITE_URL
from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils
from utils.file_utils import FileUtils


class TestChangeLanguage(BrowserUtils, FileUtils):
    @allure.feature('Language Selection')
    @allure.story('Change Language to Ukrainian')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_change_language_to_ua(self, driver):
        """
        Test to change the website language to Ukrainian and verify the language change.
        """
        # Open the homepage and close the cookie notification banner
        with allure.step("Open URL and close the cookie banner"):
            self.open_url_and_handle_notification(driver, BASE_URL)

        with allure.step("Clicking the language selector"):
            # Wait for the language selector button to be clickable, then click it.
            language_selector = self.wait_for_element_to_be_clickable(driver, HomePageLocators.LANG_SELECTOR_BTN, 20)
            language_selector.click()

        with allure.step("Selecting Ukrainian language option"):
            # Wait for the Ukrainian language option to be clickable, then select it.
            ukrainian_language_option = self.wait_for_element_to_be_clickable(driver, HomePageLocators.UA_LANG, 20)
            ukrainian_language_option.click()

        with allure.step("Verify URL and language attribute"):
            # Verify that the URL has changed to the Ukrainian version of the site.
            self.verify_url(driver, UA_WEBSITE_URL, 20)

            # Verify that the 'lang' attribute of the HTML tag is set to 'uk-UA'.
            lang_attribute = self.get_element_attribute(driver, HomePageLocators.HTML, "lang")
            assert_that(lang_attribute, equal_to("uk-UA"))

        with allure.step("Verify footer text"):
            # Handle any possible notifications again, if they reappear.
            self.handle_notification(driver)

            # Wait for the footer element to be present, then scroll to it.
            self.wait_for_element(driver, HomePageLocators.FOOTER_COPYRIGHT, 20)
            self.scroll_to_element(driver, HomePageLocators.FOOTER_COPYRIGHT)

            # Verify that the footer contains the correct Ukrainian text.
            footer_text = self.get_element_text(driver, HomePageLocators.FOOTER_COPYRIGHT)
            assert_that(footer_text, contains_string("Усі права захищено"))
