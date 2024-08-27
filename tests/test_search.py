import pytest
import allure
import logging
from hamcrest import assert_that, contains_string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL
from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils
from utils.file_utils import FileUtils


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
        try:
            with allure.step("Closing the cookie banner"):
                self.open_url(driver, BASE_URL)
                self.handle_notification(driver)

            # Click on the search icon to open the search panel
            with allure.step("Clicking the search icon"):
                search_icon = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(HomePageLocators.SEARCH_ICON)
                )
                search_icon.click()
                logging.info("Search icon clicked.")

            # Enter the search query 'AI'
            with allure.step("Entering search query"):
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(HomePageLocators.SEARCH_PANEL)
                )
                logging.info("Search panel opened and displayed.")
                search_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(HomePageLocators.SEARCH_INPUT)
                )
                search_input.send_keys("AI")
                logging.info("Search query 'AI' entered.")

            # Click the search button to submit the search
            with allure.step("Clicking the search button"):
                search_button = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(HomePageLocators.SEARCH_BUTTON_FIND)
                )
                search_button.click()
                logging.info("Search button clicked.")

            # Verify that the URL contains the search query parameter
            with allure.step("Verifying URL contains search query"):
                WebDriverWait(driver, 10).until(
                    EC.url_contains("q=AI")
                )
                current_url = driver.current_url
                assert_that(current_url, contains_string("q=AI"))
                logging.info(f"Current URL is: {current_url}")

            # Check that search results are displayed correctly
            with allure.step("Checking search results"):
                search_results_counter = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(HomePageLocators.SEARCH_RESULTS_COUNTER)
                )
                # Verify that the search results counter is displayed
                assert_that(search_results_counter.is_displayed(), "Search results counter is not displayed.")

                search_results_items = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(HomePageLocators.SEARCH_RESULTS_ITEMS)
                )
                # Scroll to the search results section for better visibility
                self.scroll_to_element(driver, HomePageLocators.SEARCH_RESULTS_ITEMS)
                assert_that(search_results_items.is_displayed(), "Search results items are not displayed.")

                # Extract the text from the search results counter and verify it contains 'AI'
                counter_text = FileUtils.get_element_text(driver, HomePageLocators.SEARCH_RESULTS_COUNTER)
                assert_that(counter_text, contains_string('AI'))
                logging.info(f"Search results counter text contains 'AI': {counter_text}")

                # Verify that the first search result item is displayed
                first_result = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(HomePageLocators.FIRST_SEARCH_RESULT)
                )
                assert_that(first_result.is_displayed(), "First search result item is not displayed.")

        except Exception as e:
            # Log and attach error details to Allure report in case of any exception
            logging.error(f"Error during search function check: {e}")
            allure.attach(f"Error: {str(e)}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise
