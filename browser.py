from selenium import webdriver


class Browser:
    def __init__(self, base_url="https://prosvirov-vladimir.github.io/test-authorization/"):
        self.driver = webdriver.Chrome()
        self.base_url = base_url

    def go_to_site(self, path):
        curl_url = self.base_url + path
        return self.driver.get(curl_url)

    def go_to_url(self, url):
        return self.driver.get(url)

    def close_browser(self):
        return self.driver.quit()

    def get_driver(self):
        return self.driver
