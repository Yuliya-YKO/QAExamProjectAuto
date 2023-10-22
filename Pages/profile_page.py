from selenium.webdriver.common.by import By


class EditProfilePage:
    def __init__(self, driver):
        self.__driver = driver
        self.__profile_button = (By.XPATH, "//span[text()='Профіль']")
        self.__edit_button = (By.XPATH, "//a[@class='user-menu__edit']")
        self.__nick_name_field = (By.XPATH, "//input[@class='ek-form-control' and @type='text']")
        self.__save_change_button = (By.XPATH, "//button[@type='submit']")
        self.__updated_user_name = (By.XPATH, "//div[@class='user-menu__name']/a[@class='info-nick']")
        self.__gender_radio_button = "//label[@class='no-select' and text()='{}']"
        self.__age_from_dropdown = "//select[@class='ek-form-control']/option[@value={}]"
        self.__age_information = "//div[text()={}]"

    def click_profile_button(self):
        profile_button = self.__driver.find_element(*self.__profile_button)
        profile_button.click()

    def click_edit_button(self):
        edit_button = self.__driver.find_element(*self.__edit_button)
        edit_button.click()

    def enter_text_in_field(self, text):
        your_nick_field = self.__driver.find_element(*self.__nick_name_field)
        your_nick_field.clear()
        your_nick_field.send_keys(text)

    def click_submit_button(self):
        submit_button = self.__driver.find_element(*self.__save_change_button)
        submit_button.click()

    def get_updated_username(self):
        updated_username = self.__driver.find_element(*self.__updated_user_name)
        current_user_name = updated_username.text
        return current_user_name

    def select_gender_radio_button(self, gender):
        # gender_radio_button = self.__driver.find_element(*self.__gender_radio_button(gender)
        xpath = self.__gender_radio_button.format(gender)
        element = self.__driver.find_element(By.XPATH, xpath)
        if not element.is_selected():
            element.click()
        else:
            print("Radio button is already selected")
        return True

    def select_age_in_dropdown(self, age):
        xpath = self.__age_from_dropdown.format(age)
        element = self.__driver.find_element(By.XPATH, xpath)
        element.click()

    def check_editing_age(self, age):
        xpath = self.__age_information.format(age)
        element = self.__driver.find_element(By.XPATH, xpath)
        element.is_displayed()
        return True


