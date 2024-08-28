import pytest
import allure
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from locators.home_page_locators import HomePageLocators
from utils.browser_utils import BrowserUtils
from config.config import BASE_URL
from constants import EXPECTED_REGIONS


class TestOurLocationsRegions(BrowserUtils):

    @allure.feature('Location Tabs Functionality')
    @allure.story('Verify switching between location lists by region')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_our_locations_regions(self, driver):
        """
        Test to verify switching between location lists by region.
        """
        # Open the target URL and handle any cookie banners or notifications.
        with allure.step("Open URL and close the cookie banner"):
            self.open_url_and_handle_notification(driver, BASE_URL)

        with allure.step("Scroll to the Locations section"):
            # Wait for the Locations section to be present on the page
            self.wait_for_element(driver, HomePageLocators.TAB_LOCATION, 20)
            # Scroll to the Locations section for visibility
            self.scroll_to_element(driver, HomePageLocators.TAB_LOCATION_SECTION)

        # Find all region tabs within the Locations section and log their texts.
        with allure.step("Find region tabs and log their texts"):
            # tabs elements
            locations_section = self.wait_for_element(driver, HomePageLocators.REGION_LIST, 30)
            region_tabs = locations_section.find_elements(*HomePageLocators.REGION_TABS)

        # Click each region tab and verify that it becomes active.
        with allure.step("Click each region tab and verify its activation"):
            for index in reversed(range(len(EXPECTED_REGIONS))):
                tab = region_tabs[index]
                tab.click()

                # Wait until the 'active' class is added to the clicked tab.
                # The tab is identified by the 'data-item' attribute using the 'index' of the current tab.
                self.wait_for_element(driver, (By.XPATH,
                                                    f"//a[contains(@class, 'tabs-23__link js-tabs-link') and @data-item='{index}' and contains(@class, 'active')]"),
                                      20)
                # Check that the 'active' class is present
                tab_class = tab.get_attribute("class")
                assert_that("active" in tab_class, equal_to(True),
                            f"Tab at index {index} does not have class 'active' after clicking it. class: {tab_class}")
