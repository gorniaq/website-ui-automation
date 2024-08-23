from selenium.webdriver.common.by import By


class AboutPageLocators:
    REPORT_DOWNLOAD_SECTION = (By.XPATH, "//*[@id='main']/div[1]/div[5]")

    DOWNLOAD_BUTTON = (By.XPATH, "//span[contains(text(),'DOWNLOAD')]")

    COMPANY_LOGO_LINK = (By.CLASS_NAME, "header__logo-link")

