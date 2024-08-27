from selenium.webdriver.common.by import By


class HomePageLocators:

    META_TITLE = (By.XPATH, "/html/head/meta[@property='og:title']")

    COOKIE_BANNER = (By.XPATH, "//*[@id='onetrust-banner-sdk']")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//*[@id='onetrust-accept-btn-handler']")

    THEME_TOGGLE = (By.XPATH, "//*[@id='wrapper']/div[2]/div[1]/header/div/div/div[2]/section/div")
    BODY = (By.TAG_NAME, "body")

    LANG_SELECTOR_BTN = (By.CSS_SELECTOR, "button.location-selector__button")
    UA_LANG = (By.XPATH, "//ul[@class='location-selector__list']//a[@href='https://careers.epam.ua']")

    HTML = (By.TAG_NAME, "html")
    FOOTER = (By.XPATH, "//footer//div[@class='footer-inner']")
    FOOTER_COPYRIGHT = (By.CSS_SELECTOR, "div.footer__copyright")

    TAB_LOCATION = (By.ID, "id-890298b8-f4a7-3f75-8a76-be36dc4490fd")
    TAB_LOCATION_SECTION = (By.XPATH, "//*[@id='main']/div[1]/div[16]")
    REGION_LIST = (By.XPATH, "//div[@class='js-tabs-controls']")
    REGION_TABS = (By.XPATH, "//div[contains(@class, 'tabs-23__title') and contains(@class, 'js-tabs-title')]")

    POLICIES_SECTION = (By.CLASS_NAME, "policies")
    POLICY_LINKS = (By.CSS_SELECTOR, "ul li a")

    SEARCH_ICON = (By.CLASS_NAME, "search-icon")
    SEARCH_PANEL = (By.CSS_SELECTOR, "div.header-search__panel.opened[style*='display: block;']")

    SEARCH_INPUT = (By.ID, "new_form_search")
    SEARCH_BUTTON_FIND = (By.XPATH, "//button[contains(@class, 'custom-search-button')]")
    SEARCH_RESULTS_COUNTER = (By.XPATH, "//h2[@class='search-results__counter']")
    SEARCH_RESULTS_ITEMS = (By.CLASS_NAME, "search-results__items")
    FIRST_SEARCH_RESULT = (By.CSS_SELECTOR, ".search-results__items .search-results__item")
    TARGET_ELEMENT = (By.ID, "id-6563fe11-2f96-386e-92ae-b843b1712be5")



