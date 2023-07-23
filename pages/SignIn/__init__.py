from pages.SignIn.Locators import Locators
from pages.SignIn.Element import *
import random
import string


class User:
    def __init__(self, email):
        self.email = email

    @staticmethod
    def generate_password(count_special_chars, count_letters, count_numbers):
        special_chars = random.sample(string.punctuation, count_special_chars)
        letters = random.sample(string.ascii_letters, count_letters)
        numbers = random.sample(string.digits, count_numbers)
        password = special_chars + letters + numbers
        return password

    # Пароль должен содержать минимум 8 символов, хотя бы одну букву,
    # хотя бы одну цифру и хотя бы один специальный знак.
    def password(self):
        self.password = self.generate_password(count_special_chars=1, count_numbers=2, count_letters=5)
        return self.password


class SignIn:
    path = "login.html"

    def __init__(self, browser):
        self.email = InputElement(driver=browser.get_driver(), locator=Locators.email_locator)
        self.password = InputElement(driver=browser.get_driver(), locator=Locators.password_locator)
        self.button = ButtonElement(driver=browser.get_driver(), locator=Locators.button_login_locator)

    def signin(self, user: User):
        self.email.enter_text(user.email)
        self.password.enter_text(user.password())
        self.button.click_element()
