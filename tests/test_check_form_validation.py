import pytest
import allure
import re
from hamcrest import assert_that, is_, less_than_or_equal_to, not_none
from selenium.webdriver.common.by import By

from config.config import CONTACT_URL
from constants import FORM_FIELD_VALUES
from locators.contacts_page_locators import ContactsPageLocators
from utils.browser_utils import BrowserUtils


class TestFormsFieldsValidation(BrowserUtils):
    @allure.feature('Form Validation Check')
    @allure.story('Verify required fields in the contact form')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_check_required_fields(self, driver):

        # Open the target URL and handle any cookie banners or notifications.
        with allure.step("Open URL and close the cookie banner"):
            self.open_url_and_handle_notification(driver, CONTACT_URL)

        with allure.step("Waiting for the form to be present and scrolling to it"):
            # Wait for the form to be present and scroll to it
            self.wait_for_element(driver, ContactsPageLocators.FORM, 20)
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
                assert_that(field_type, is_("text"),
                            f"Field '{name}' is expected to be of type 'text', but got '{field_type}'.")

                # Clear any existing text in the input field
                field.clear()
                # Enter the provided value into the input
                field.send_keys(value)

                if name == "user_email":
                    assert_that("@" in field.get_attribute("value"), is_(True),
                                f"Field '{name}' should contain '@' symbol for a valid email address.")

                if name == "user_phone":
                    phone_value = field.get_attribute("value")
                    assert_that(re.match(r'^[0-9\s\+;]*$', phone_value), is_(not_none()),
                                "Phone number contains invalid characters")
                    assert_that(len(phone_value), is_(less_than_or_equal_to(13)),
                                f"Phone number '{phone_value}' exceeds the allowed length of 13 digits.")
