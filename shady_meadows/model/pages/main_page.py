import allure
from selene import browser


class MainPage:

    def __init__(self):
        self.open_booking_button = browser.element('.openBooking')


    @allure.step('Открываем стартовую страницу')
    def open(self):
        browser.open('/')


    @allure.step('Открываем форму бронирования')
    def press_open_booking_button(self):
        self.open_booking_button.click()