from selenium.webdriver.common.by import By


class HomePageLocators:

    META_TITLE = (By.XPATH, "/html/head/meta[@property='og:title']")

    COOKIE_BANNER = (By.XPATH, "//*[@id='onetrust-banner-sdk']")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//*[@id='onetrust-accept-btn-handler']")

    THEME_TOGGLE = (By.XPATH, "//*[@id='wrapper']/div[2]/div[1]/header/div/div/div[2]/section/div")
    BODY = (By.TAG_NAME, "body")

    LANG_SELECTOR_BTN = (By.CSS_SELECTOR, "button.location-selector__button")
    UA_LANG = (By.XPATH, "//ul[@class='location-selector__list']//a[@href='https://careers.epam.ua']")

    HTML = By.TAG_NAME, "html"
    FOOTER = (By.XPATH, "//footer//div[@class='footer-inner']")
    FOOTER_COPYRIGHT = By.CSS_SELECTOR, "div.footer__copyright"

    POLICIES_SECTION = (By.CLASS_NAME, "policies")
    POLICY_LINKS = (By.CSS_SELECTOR, "ul li a")



