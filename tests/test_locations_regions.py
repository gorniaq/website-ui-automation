import pytest
import allure
import logging
import time
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils
from config.config import BASE_URL, EXPECTED_REGIONS


class TestOurLocationsRegions(BrowserUtils):

    @allure.feature('Location Tabs Functionality')
    @allure.story('Verify switching between location lists by region')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_our_locations_regions(self, driver):
        """
        Test to verify switching between location lists by region.
        Args:
            driver (webdriver): The WebDriver instance used for testing.
        Raises:
            Exception: If any error occurs during the test.
        """
        try:
            with allure.step("Open URL and close the cookie banner"):
                # Open the target URL and handle any cookie banners or notifications.
                self.open_url(driver, BASE_URL)
                self.handle_notification(driver)

            with allure.step("Scroll to the Locations section"):
                # Wait for the Locations section to be present on the page
                locations_section = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(HomePageLocators.TAB_LOCATION)
                )
                # Scroll to the Locations section for visibility
                self.scroll_to_element(driver, HomePageLocators.TAB_LOCATION_SECTION)
                logging.info("Our Locations section found")
                time.sleep(3)

            # Find all region tabs within the Locations section and log their texts.
            with allure.step("Find region tabs and log their texts"):
                # tabs elements
                locations_section = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(HomePageLocators.REGION_LIST)
                )
                region_tabs = locations_section.find_elements(*HomePageLocators.REGION_TABS)
                # Extract and log the text of each region tab
                region_texts = [tab.text.strip().upper() for tab in region_tabs]
                logging.info(f"Found regions: {region_texts}")

            # Click each region tab and verify that it becomes active.
            with allure.step("Click each region tab and verify its activation"):
                for index in reversed(range(len(EXPECTED_REGIONS))):
                    tab = region_tabs[index]
                    tab.click()

                    # Wait until the 'active' class is added to the clicked tab.
                    # The tab is identified by the 'data-item' attribute using the 'index' of the current tab.
                    WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        f"//a[contains(@class, 'tabs-23__link js-tabs-link') and @data-item='{index}' and contains(@class, 'active')]"))
                    )

                    # Check that the 'active' class is present
                    tab_class = tab.get_attribute("class")
                    assert_that("active" in tab_class, equal_to(True),
                                f"Tab at index {index} does not have class 'active' after clicking it. class: {tab_class}")

                    logging.info(f"Tab at index {index} is active after clicking it and has class 'active'.")
                    allure.attach(f"Tab {index} class: {tab_class}",
                                  name=f"Tab {index} Activation Status",
                                  attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            logging.error(f"Error during Our Locations regions check: {e}")
            allure.attach(f"Error: {str(e)}", name="Error Details", attachment_type=allure.attachment_type.TEXT)
            raise

