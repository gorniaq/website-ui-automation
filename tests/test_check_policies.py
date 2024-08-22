import logging
import allure
import pytest
from hamcrest import assert_that, has_item, equal_to
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL, EXPECTED_POLICIES
from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils


class TestPoliciesList(BrowserUtils):
    @allure.feature('Policies List')
    @allure.story('Verify policies list on the page')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_policies_list(self, driver):
        """
        Test to verify the policies list on the page.
        Raises:
            Exception: Error during policies list verification.
        """
        try:
            with allure.step("Open URL and close the cookie banner"):
                # Open the specified URL in the browser and close any cookie banners that appear.
                self.open_url(driver, BASE_URL)
                self.handle_notification(driver)

            with allure.step("Scroll to the footer and locate the policies section"):
                # Scroll down the webpage to the footer where the policies section is located.
                self.scroll_to_element(driver, HomePageLocators.FOOTER)
                logging.info("Scrolled to the footer")

                # Wait until the policies section becomes visible on the page.
                policies_section = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(HomePageLocators.POLICIES_SECTION)
                )
                logging.info("Policies section found")

            with allure.step("Extract and log policy links"):
                # Find all the policy links within the policies section.
                policy_links = policies_section.find_elements(*HomePageLocators.POLICY_LINKS)

                # Extract and clean the text from each policy link.
                policy_texts = [link.text.strip() for link in policy_links]
                logging.info(f"Found policies: {policy_texts}")

            with allure.step("Verify the count of policies"):
                # Verify that the number of policies found matches the expected number.
                expected_count = len(EXPECTED_POLICIES)
                actual_count = len(policy_texts)
                assert_that(actual_count, equal_to(expected_count),
                            f"Expected {expected_count} policies, but found {actual_count}.")

            with allure.step("Verify that all expected policies are present"):
                # Check that each expected policy is present in the list of policies found on the page.
                for policy in EXPECTED_POLICIES:
                    assert_that(policy_texts, has_item(policy))
                logging.info("All expected policies are present in the list")

        except Exception as e:
            logging.error(f"Error during policies list check: {e}")
            allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot",
                         attachment_type=allure.attachment_type.PNG)
            allure.attach(f"Error: {e}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise
