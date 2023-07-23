from selenium.webdriver import Keys


class Element:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = self.driver.find_element(self.locator[0], self.locator[1])

    def click_element(self):
        self.element.click()


class InputElement(Element):
    def enter_text(self, text):
        self.click_element()
        self.element.send_keys(text)

    def key_enter(self):
        return self.element.send_keys(Keys.ENTER)

    def get_text(self):
        return self.element.get_attribute("value")


class ButtonElement(Element):
    def key_click(self):
        return self.element.send_keys(Keys.ENTER)
