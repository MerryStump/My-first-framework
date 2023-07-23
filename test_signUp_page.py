import pytest
from pages.SignUp import SignUp, User
from browser import Browser


@pytest.fixture()
def user_test():
    return User(first_name="Test", last_name="User", email="Test@test.ru", organization="Atach", country="Россия", phone="+7-999-999-99-99")


@pytest.fixture()
def browser():
    return Browser()


class TestSignUpPage:

    def test_signup(self, browser, user_test):
        browser.go_to_site(SignUp.path)
        browser.driver.implicitly_wait(10)
        page = SignUp(browser)
        page.signup(user_test)
