from selenium.webdriver.common.by import By


class Locators:
    first_name_locator = (By.ID, "registrationFirstNameInp")
    last_name_locator = (By.ID, "registrationLastNameInp")
    email_locator = (By.ID, "registrationEmailInp")
    password_locator = (By.ID, "registrationPasswordInp")
    organization_locator = (By.ID, "registrationCompanyInp")
    # Locator поля
    country_locator = (By.CSS_SELECTOR, "#registrationCountryInp")
    # Locator значения
    country_locator_value = (By.ID, "countryDropdownList")
    phone_locator = (By.ID, "registrationPhoneInp")
    checkbox_locator = (By.ID, "agreementChkbox")
    button_registration_locator = (By.ID, "registrationSignUpBtn")
    error_massage_locator = (By.ID, "registrationMessage")
    login_link_locator = (By.ID, "/html/body/div/a")
