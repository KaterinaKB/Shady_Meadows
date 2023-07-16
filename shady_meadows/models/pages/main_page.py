from selene import browser


class MainPage:

    def __init__(self):
        self.open_booking_button = browser.element('.openBooking')


    def open(self):
        browser.open('/')


    def press_open_booking_button(self):
        self.open_booking_button.click()