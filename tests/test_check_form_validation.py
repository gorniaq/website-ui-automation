import time

import pytest
import allure
import logging
from hamcrest import assert_that, contains_string, is_
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL, CONTACT_URL, FORM_FIELD_VALUES
from locators.contacts_page_locators import ContactsPageLocators
from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils
from utils.file_utils import FileUtils


class TestFormsFieldsValidation(BrowserUtils):

    @allure.feature('Form Validation Check')
    @allure.story('Verify required fields in the contact form')
    def test_check_required_fields(self, driver):

        try:
            with allure.step("Closing the cookie banner"):
                self.open_url(driver, CONTACT_URL)
                self.handle_notification(driver)

            with allure.step("Waiting for the form to be present and scrolling to it"):
                form = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(ContactsPageLocators.FORM)
                )
                self.scroll_to_element(driver, ContactsPageLocators.CONTACT_SECTION)


            # for name, value in FORM_FIELD_VALUES.items():
            #     with allure.step(f"Validating field '{name}'"):
            #         field = driver.find_element(By.NAME, name)
            #
            #         # Check if the field is required
            #         is_required = field.get_attribute("required")
            #         assert_that(is_required, is_(True), f"Field '{name}' is not marked as required")
            #         allure.attach(str(is_required), name=f"Field '{name}' Required Status",
            #                       attachment_type=allure.attachment_type.TEXT)
            #
            #         # Check the field type
            #         field_type = field.get_attribute("type")
            #         assert_that(field_type, is_("text"))
            #         allure.attach(field_type, name=f"Field '{name}' Type", attachment_type=allure.attachment_type.TEXT)
            #
            #         # Input validation
            #         field.clear()
            #         field.send_keys(value)
            #         field_value = field.get_attribute("value")
            #         allure.attach(field_value, name=f"Field '{name}' Value", attachment_type=allure.attachment_type.TEXT)
            #
            #         if name == "user_email":
            #             email_pattern = r"[^@]+@[^@]+\.[^@]+"
            #             assert_that(re.match(email_pattern, field_value), is_(not_none()), "Email does not match pattern")
            #             allure.attach("Field 'user_email' matches the email pattern", name="Email Validation Status",
            #                           attachment_type=allure.attachment_type.TEXT)
            #
            #         if name == "user_phone":
            #             phone_value = field.get_attribute("value")
            #             assert_that(re.match(r'^[0-9\s\+;]*$', phone_value), is_(not_none()),
            #                         "Phone number contains invalid characters")
            #             assert_that(len(phone_value), is_(less_than_or_equal_to(50)), "Phone number exceeds maximum length")
            #             allure.attach(phone_value, name="Phone Field Value", attachment_type=allure.attachment_type.TEXT)
            #
            # with allure.step("All fields validated"):
            #     allure.attach("All fields are validated", name="Validation Summary",
            #                   attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            logging.error(f"Error during form validation check: {e}")
            allure.attach(f"Error: {str(e)}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise
