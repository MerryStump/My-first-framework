from selenium.webdriver.common.by import By


class Locators:
    email_locator = (By.ID, "loginEmailInp")
    password_locator = (By.ID, "loginPasswordInp")
    button_login_locator = (By.ID, "loginBtn")
