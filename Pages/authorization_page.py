from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AuthorizationPage:
    __URL = 'https://ek.ua/ua/'

    def __init__(self, driver):
        self.__driver = driver
        self.__login_button = (By.XPATH, "//span[text()='Увійти']")
        self.__nick_button_success_login = (By.XPATH, "//a[@class='info-nick']")
        self.__profile = (By.XPATH, "//a[@class='info-nick']")
        self.__logout = (By.XPATH, "//a[@jtype='click']/em[@title='Вийти']")
        self.__errors_registration = (By.XPATH, "//div[@class='ek-form-text']")
        self.__login_by_email = (By.XPATH, "//div[text()='E-mail']")
        self.__name_field_for_login = (By.XPATH, "//input[@placeholder ='E-Mail або Логін']")
        self.__password_for_login = (By.XPATH, "//input[@placeholder ='Пароль' and @autocomplete ='current-password']")
        self.__submit_login_button = (By.XPATH, "//button[text() ='УВІЙТИ']")
        self.__error_email_not_entered = (By.XPATH, "//div[text() = 'Введіть логін/email!']")
        self.__error_password_not_entered = (By.XPATH, "//div[text() = 'Введіть пароль!']")
        self.__error_wrong_email = (By.XPATH, "//div[@class='ek-form-text']/b")
        self.__error__wrong_password = (By.XPATH, "//div[text() = 'Пароль вказаний невірно!']")

    def open(self):
        self.__driver.get(self.__URL)

    def click_login_button(self):
        login_button = self.__driver.find_element(*self.__login_button)
        WebDriverWait(self.__driver, 10).until(ec.visibility_of(login_button))
        login_button.click()

    def click_nick_name_button(self):
        nick_name_button = self.__driver.find_element(*self.__nick_button_success_login)
        nick_name_button.click()

    def choose_login_by_email(self):
        login_email = self.__driver.find_element(*self.__login_by_email)
        WebDriverWait(self.__driver, 10).until(ec.visibility_of(login_email))
        login_email.click()

    def enter_text_in_field(self, web_element, text):
        try:
            web_element.clear()
            web_element.send_keys(text)
        except (NoSuchElementException, ElementNotInteractableException) as e:
            self.print_error_and_stop_test(e)

    def print_error_and_stop_test(self, exception):
        raise AssertionError(f"Cannot work with element: {exception}")

    def enter_email_for_login(self, email):
        login_by_email_field = self.__driver.find_element(*self.__name_field_for_login)
        self.enter_text_in_field(login_by_email_field, email)

    def enter_password_for_login(self, password):
        password_field = self.__driver.find_element(*self.__password_for_login)
        self.enter_text_in_field(password_field, password)

    def input_in_login_form(self, email, password):
        login_by_email_button = self.__driver.find_element(*self.__login_by_email)
        login_by_email_button.click()

        # submit_login_button = self.__driver.find_element(*self.__submit_login_button)
        # WebDriverWait(self.__driver, 10).until(ec.visibility_of(submit_login_button))

        self.enter_email_for_login(email)
        self.enter_password_for_login(password)

    def is_logged_in(self):
        try:
            WebDriverWait(self.__driver, 10).until(
                ec.presence_of_element_located(self.__nick_button_success_login)
            )
            return True
        except NoSuchElementException:
            return False

    def click_on_submit_login_button(self):
        submit_login_button = self.__driver.find_element(*self.__submit_login_button)
        submit_login_button.click()

    def check_for_errors(self):
        error_messages = []

        try:
            self.__driver.find_element(*self.__error_email_not_entered)
            error_messages.append("Введіть логін/email!")
        except NoSuchElementException:
            pass

        try:
            self.__driver.find_element(*self.__error_password_not_entered)
            error_messages.append("Введіть пароль!")
        except NoSuchElementException:
            pass

        try:
            self.__driver.find_element(*self.__error_wrong_email)
            error_messages.append("Помилковий логін/email!")
        except NoSuchElementException:
            pass

        try:
            self.__driver.find_element(*self.__error__wrong_password)
            error_messages.append("Пароль вказаний невірно!")
        except NoSuchElementException:
            pass

        return error_messages
