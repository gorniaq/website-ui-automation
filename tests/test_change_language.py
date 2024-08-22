import logging
import pytest
import allure
from hamcrest import assert_that, contains_string, equal_to
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        Raises:
            Exception: If any error occurs during the test.
        """
        try:
            with allure.step("Open URL and closing the cookie banner"):
                # Open the base URL and handle any cookie banners or notifications.
                self.open_url(driver, BASE_URL)
                self.handle_notification(driver)

            with allure.step("Clicking the language selector"):
                # Wait for the language selector button to be clickable, then click it.
                language_selector = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(HomePageLocators.LANG_SELECTOR_BTN)
                )
                language_selector.click()
                logging.info("Language selector clicked")

            with allure.step("Selecting Ukrainian language option"):
                # Wait for the Ukrainian language option to be clickable, then select it.
                ukrainian_language_option = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(HomePageLocators.UA_LANG)
                )
                ukrainian_language_option.click()
                logging.info("Ukrainian language selected")

            with allure.step("Verify URL and language attribute"):
                # Verify that the URL has changed to the Ukrainian version of the site.
                WebDriverWait(driver, 20).until(
                    EC.url_to_be(UA_WEBSITE_URL)
                )
                logging.info("URL verified")

                # Verify that the 'lang' attribute of the HTML tag is set to 'uk-UA'.
                lang_attribute = self.get_element_attribute(driver, HomePageLocators.HTML, "lang")
                assert_that(lang_attribute, equal_to("uk-UA"))
                logging.info("Lang attribute verified")
                allure.attach(f"Lang attribute: {lang_attribute}", name="Language Attribute Verification",
                              attachment_type=allure.attachment_type.TEXT)

            with allure.step("Verify footer text"):
                # Handle any possible notifications again, if they reappear.
                self.handle_notification(driver)

                # Wait for the footer element to be present, then scroll to it.
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(HomePageLocators.FOOTER_COPYRIGHT)
                )
                self.scroll_to_element(driver, HomePageLocators.FOOTER_COPYRIGHT)

                # Verify that the footer contains the correct Ukrainian text.
                footer_text = self.get_element_text(driver, HomePageLocators.FOOTER_COPYRIGHT)
                assert_that(footer_text, contains_string("Усі права захищено"))
                logging.info("Language change to Ukrainian verified successfully")
                allure.attach(f"Footer text: {footer_text}", name="Footer Text Verification",
                              attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            # Log the error, attach a screenshot and error details to the allure report, then raise the exception.
            logging.error(f"Error during language change check: {e}")
            allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(f"Error: {str(e)}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise
