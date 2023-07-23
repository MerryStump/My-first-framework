from pages.SignUp.Locators import Locators
from pages.SignUp.Element import *
import random
import string
import time


class User:
    def __init__(self, first_name, last_name, email, organization, country, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.organization = organization
        self.country = country
        self.phone = phone

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


class SignUp:
    path = "sign-up.html"

    def __init__(self, browser):
        self.first_name = InputElement(driver=browser.get_driver(), locator=Locators.first_name_locator)
        self.last_name = InputElement(driver=browser.get_driver(), locator=Locators.last_name_locator)
        self.email = InputElement(driver=browser.get_driver(), locator=Locators.email_locator)
        self.password = InputElement(driver=browser.get_driver(), locator=Locators.password_locator)
        self.organization = InputElement(driver=browser.get_driver(), locator=Locators.organization_locator)
        self.country = InputElement(driver=browser.get_driver(), locator=Locators.country_locator)
        self.country_click = InputElement(driver=browser.get_driver(), locator=Locators.country_locator_value)
        self.phone = InputElement(driver=browser.get_driver(), locator=Locators.phone_locator)
        self.checkbox = CheckBoxElement(driver=browser.get_driver(), locator=Locators.checkbox_locator)
        self.button = ButtonElement(driver=browser.get_driver(), locator=Locators.button_registration_locator)

    def signup(self, user: User):
        self.first_name.enter_text(user.first_name)

        self.last_name.enter_text(user.last_name)

        self.email.enter_text(user.email)

        self.password.enter_text(user.password())

        self.organization.enter_text(user.organization)

        self.country.enter_text(user.country)

        # выбрать найденный город
        self.country_click.click_element()

        self.phone.enter_text(user.phone)

        self.checkbox.check()

        self.button.click_element()
