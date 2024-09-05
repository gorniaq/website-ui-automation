import pytest
import allure
from hamcrest import assert_that, has_item, equal_to

from constants import EXPECTED_POLICIES
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
        # Open the homepage and close the cookie notification banner
        with allure.step("Open URL and close the cookie banner"):
            self.open_url_and_handle_notification(driver)

        with allure.step("Scroll to the footer and locate the policies section"):
            # Scroll down the webpage to the footer where the policies section is located.
            self.scroll_to_element(driver, HomePageLocators.FOOTER)

            # Wait until the policies section becomes visible on the page.
            policies_section = self.wait_for_element(driver, HomePageLocators.POLICIES_SECTION)

        with allure.step("Extract and log policy links"):
            # Find all the policy links within the policies section.
            policy_links = policies_section.find_elements(*HomePageLocators.POLICY_LINKS)
            # Extract and clean the text from each policy link.
            policy_texts = [link.text.strip() for link in policy_links]

        with allure.step("Verify the count of policies"):
            # Verify that the number of policies found matches the expected number.
            expected_count = len(EXPECTED_POLICIES)
            actual_count = len(policy_texts)
            assert_that(actual_count, equal_to(expected_count),
                        f"Expected {expected_count} policies, but found {actual_count}.")

        with allure.step("Verify that all expected policies are present"):
            # Check that each expected policy is present in the list of policies found on the page.
            for policy in EXPECTED_POLICIES:
                assert_that(policy_texts, has_item(policy),
                            f"Expected policy '{policy}' is not found in the list of policies: {policy_texts}")
