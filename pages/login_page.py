from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        page_url = str(self.browser.current_url)
        assert 'login' in page_url, "incorrect login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def should_be_email_input(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_INPUT)

    def should_be_password_input(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_INPUT)

    def should_be_password2_input(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_INPUT)

    def should_be_inputs(self):
        self.should_be_register_form()
        self.should_be_password_input()
        self.should_be_password2_input()

    def register_new_user(self, email, password):
        self.browser.get(LoginPageLocators.LOGIN_LINK)
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT).click()

