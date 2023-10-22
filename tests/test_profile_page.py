from Pages.authorization_page import AuthorizationPage
from Pages.profile_page import EditProfilePage


correct_email = 'yko.kot@gmail.com'
correct_password = 123456789
new_name = "Юлія"
gender_male = 'Ч'
gender_female = 'Ж'
check_gender_male = "чоловіча"
check_gender_female = "женский"
age = ' 1999'


class TestEditProfile:

    def test_edit_nick_name(self, chrome):
        page_auth = AuthorizationPage(chrome)
        profile_page = EditProfilePage(chrome)
        page_auth.open()
        page_auth.click_login_button()
        page_auth.input_in_login_form(correct_email, correct_password)
        page_auth.click_on_submit_login_button()
        page_auth.click_nick_name_button()
        profile_page.click_profile_button()
        profile_page.click_edit_button()
        profile_page.enter_text_in_field(new_name)
        profile_page.click_submit_button()
        assert profile_page.get_updated_username() == new_name

    def test_edit_gender(self, chrome):
        page_auth = AuthorizationPage(chrome)
        profile_page = EditProfilePage(chrome)
        page_auth.open()
        page_auth.click_login_button()
        page_auth.input_in_login_form(correct_email, correct_password)
        page_auth.click_on_submit_login_button()
        page_auth.click_nick_name_button()
        profile_page.click_profile_button()
        profile_page.click_edit_button()
        assert profile_page.select_gender_radio_button(gender_male)

    def test_edit_age(self, chrome):
        page_auth = AuthorizationPage(chrome)
        profile_page = EditProfilePage(chrome)
        page_auth.open()
        page_auth.click_login_button()
        page_auth.input_in_login_form(correct_email, correct_password)
        page_auth.click_on_submit_login_button()
        page_auth.click_nick_name_button()
        profile_page.click_profile_button()
        profile_page.click_edit_button()
        profile_page.select_age_in_dropdown(age)
        profile_page.click_submit_button()
        assert profile_page.check_editing_age(age)



