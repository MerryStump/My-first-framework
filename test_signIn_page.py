import pytest
from pages.SignIn import SignIn, User
from browser import Browser


@pytest.fixture()
def user_test():
    return User(email="Test@test.ru")


@pytest.fixture()
def browser():
    return Browser()


class TestSignUpPage:

    def test_signup(self, browser, user_test):
        browser.go_to_site(SignIn.path)
        browser.driver.implicitly_wait(10)
        page = SignIn(browser)
        page.signin(user_test)
