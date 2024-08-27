import pytest
import allure
import logging
from hamcrest import assert_that, is_, less_than_or_equal_to, not_none
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from config.config import CONTACT_URL, FORM_FIELD_VALUES
from locators.contacts_page_locators import ContactsPageLocators
from utils.browser_utils import BrowserUtils


class TestFormsFieldsValidation(BrowserUtils):

    @allure.feature('Form Validation Check')
    @allure.story('Verify required fields in the contact form')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_check_required_fields(self, driver):

        try:
            with allure.step("Closing the cookie banner"):
                # Open the contact URL and handle any notifications
                self.open_url(driver, CONTACT_URL)
                self.handle_notification(driver)

            with allure.step("Waiting for the form to be present and scrolling to it"):
                # Wait for the form to be present and scroll to it
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(ContactsPageLocators.FORM)
                )
                self.scroll_to_element(driver, ContactsPageLocators.CONTACT_SECTION)

            # Validate each form field
            for name, value in FORM_FIELD_VALUES.items():
                with allure.step(f"Validating field '{name}'"):
                    field = driver.find_element(By.NAME, name)

                    # Check if the field is required
                    is_required = field.get_attribute("aria-required")
                    assert_that(is_required, is_("true"), f"Field '{name}' is not marked as required")

                    # Check the field type
                    field_type = field.get_attribute("type")
                    assert_that(field_type, is_("text"))

                    # Input validation
                    # Clear any existing text in the input field
                    field.clear()
                    # Enter the provided value into the input
                    field.send_keys(value)
                    # Retrieve the value of the input field to verify it was set correctly
                    field_value = field.get_attribute("value")
                    allure.attach(field_value, name=f"Field '{name}' Value",
                                  attachment_type=allure.attachment_type.TEXT)
                    logging.info(f"Field '{name}' has been set to value: {field_value}")

                    if name == "user_email":
                        assert_that("@" in field.get_attribute("value"), is_(True))
                        logging.info("Field 'user_email' contains '@'")

                    if name == "user_phone":
                        phone_value = field.get_attribute("value")
                        assert_that(re.match(r'^[0-9\s\+;]*$', phone_value), is_(not_none()))
                        assert_that(len(phone_value), is_(less_than_or_equal_to(50)))
                        logging.info("Field 'user_phone' is validated for allowed characters and length")

            with allure.step("All fields validated"):
                logging.info("All fields are validated")

        except Exception as e:
            logging.error(f"Error during form validation check: {e}")
            allure.attach(f"Error: {str(e)}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise
