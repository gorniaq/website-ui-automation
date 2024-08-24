from selenium.webdriver.common.by import By


class AboutPageLocators:

    COMPANY_LOGO_LINK = (By.CLASS_NAME, "header__logo-link")

    REPORT_DOWNLOAD_SECTION = (By.XPATH, "(//div[@class='column-control'])[2]")
    DOWNLOAD_BUTTON = (By.XPATH, "//span[contains(text(),'DOWNLOAD')]")


