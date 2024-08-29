import pytest
import allure
import logging
from hamcrest import assert_that, contains_string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL
from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils


class TestSearchFunction(BrowserUtils):

    @allure.feature("Search Functionality")
    @allure.story("Check the search function works correctly")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_search_function(self, driver):
        """
        Test case to verify the search functionality on the homepage.
        Raises:
            Exception: If any error occurs during the test.
        """
        # Open the homepage and close the cookie notification banner
        with allure.step("Open URL and close the cookie banner"):
            self.open_url_and_handle_notification(driver, BASE_URL)

        # Click on the search icon to open the search panel
        with allure.step("Clicking the search icon"):
            self.wait_for_element_and_click(driver, HomePageLocators.SEARCH_ICON, 20)

        # Enter the search query 'AI'
        with allure.step("Entering search query"):
            self.wait_for_element(driver, HomePageLocators.SEARCH_PANEL, 20)
            search_input = self.wait_for_element(driver, HomePageLocators.SEARCH_INPUT, 20)
            search_input.send_keys("AI")

        # Click the search button to submit the search
        with allure.step("Clicking the search button"):
            self.wait_for_element_and_click(driver, HomePageLocators.SEARCH_BUTTON_FIND, 30)

        # Verify that the URL contains the search query parameter
        with allure.step("Verifying URL contains search query"):
            WebDriverWait(driver, 10).until(
                EC.url_contains("q=AI")
            )
            current_url = driver.current_url
            assert_that(current_url, contains_string("q=AI"),
                        f"Expected 'q=AI' in URL but got: {current_url}")

        # Check that search results are displayed correctly
        with allure.step("Checking search results"):
            search_results_counter = self.wait_for_element(driver, HomePageLocators.SEARCH_RESULTS_COUNTER, 20)
            # Verify that the search results counter is displayed
            assert_that(search_results_counter.is_displayed(), "Search results counter is not displayed.")

            search_results_items = self.wait_for_element(driver, HomePageLocators.SEARCH_RESULTS_ITEMS, 20)

            # Scroll to the search results section for better visibility
            self.scroll_to_element(driver, HomePageLocators.SEARCH_RESULTS_ITEMS)
            assert_that(search_results_items.is_displayed(), "Search results items are not displayed.")

            # Extract the text from the search results counter and verify it contains 'AI'
            counter_text = self.get_element_text(driver, HomePageLocators.SEARCH_RESULTS_COUNTER)
            assert_that(counter_text, contains_string('AI'),
                        f"Expected search counter to contain 'AI' but got: {counter_text}")

            # Verify that the first search result item is displayed
            first_result = self.wait_for_element(driver, HomePageLocators.FIRST_SEARCH_RESULT, 20)
            assert_that(first_result.is_displayed(), "First search result item is not displayed.")
