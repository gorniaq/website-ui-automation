from selenium.webdriver.common.by import By


class ContactsPageLocators:
    # Example locators for the contact form
    FORM = (By.TAG_NAME, "form")
    CONTACT_SECTION = (By.XPATH, "//div[contains(@class, 'form-constructor') and contains(@class, 'start')]")