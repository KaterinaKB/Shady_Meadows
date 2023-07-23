import allure
from selene import browser, have, be

from project_config import project_config


class AdminPage:

    def __init__(self):
        self.open_booking_button = browser.element('.openBooking')
        self.login_field = browser.element('#username')
        self.password_field = browser.element('#password')
        self.login_button = browser.element('#doLogin')
        self.messages_button = browser.element('.fa-inbox')

    @allure.step('Открываем страницу администратора')
    def open(self):
        browser.open('/#/admin')

    @allure.step('Вводим логин администратора')
    def fill_login(self):
        self.login_field.type(project_config.admin_login)
        return self

    @allure.step('Вводим пароль администратора')
    def fill_password(self):
        self.password_field.type(project_config.admin_pwd)
        return self

    @allure.step('Нажимаем на кнопку авторизации')
    def press_login_button(self):
        self.login_button.click()

    @allure.step('Авторизуемся в качестве администратора')
    def login(self):
        self.open()
        self.fill_login().fill_password().press_login_button()

    @allure.step('Переходим на страницу с сообщениями')
    def go_to_messages_page(self):
        self.messages_button.click()
