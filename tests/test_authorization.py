from time import sleep

import pytest
from Pages.authorization_page import AuthorizationPage

invalid_email = 'jffjfj@jghgh.fjj'
invalid_password = 1234567
correct_email = 'yko.kot@gmail.com'
correct_password = 123456789


class TestAuth:
    @pytest.mark.smoke
    def test_successful_login(self, chrome):
        page = AuthorizationPage(chrome)
        page.open()
        page.click_login_button()
        page.input_in_login_form(correct_email, correct_password)
        page.click_on_submit_login_button()
        assert page.is_logged_in()

    @pytest.mark.smoke
    def test_invalid_login(self, chrome):
        page = AuthorizationPage(driver=chrome)
        page.open()
        page.click_login_button()
        page.input_in_login_form(invalid_email, invalid_password)
        page.click_on_submit_login_button()
        error_messages = page.check_for_errors()
        assert "Помилковий логін/email!" in error_messages

    @pytest.mark.smoke
    def test_empty_fields(self, chrome):
        page = AuthorizationPage(driver=chrome)
        page.open()
        page.click_login_button()
        page.choose_login_by_email()
        page.click_on_submit_login_button()
        sleep(2)
        error_messages = page.check_for_errors()
        assert "Введіть логін/email!" in error_messages
        assert "Введіть пароль!" in error_messages

    @pytest.mark.smoke
    def test_empty_email_field(self, chrome):
        page = AuthorizationPage(driver=chrome)
        page.open()
        page.click_login_button()
        page.choose_login_by_email()
        page.enter_password_for_login(correct_password)
        page.click_on_submit_login_button()
        sleep(2)
        error_messages = page.check_for_errors()
        assert "Введіть логін/email!" in error_messages

    @pytest.mark.smoke
    def test_empty_password_field(self, chrome):
        page = AuthorizationPage(driver=chrome)
        page.open()
        page.click_login_button()
        page.input_in_login_form(correct_email, invalid_password)
        page.click_on_submit_login_button()
        sleep(2)
        error_messages = page.check_for_errors()
        assert "Пароль вказаний невірно!" in error_messages
