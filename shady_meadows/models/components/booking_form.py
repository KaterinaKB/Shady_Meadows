from selene import browser, have
from selene import command
from shady_meadows.models.utils import actions


class BookingForm:
    def __init__(self):
        self.firstname = browser.element('[name=firstname]')
        self.lastname = browser.element('[name=lastname]')
        self.email = browser.element('[name=email]')
        self.phone = browser.element('[name=phone]')
        self.start_day = browser.all('button[role=cell]').element_by(have.exact_text('01'))
        self.target_day = browser.all('button[role=cell]').element_by(have.exact_text('02'))
        self.book_button = browser.all('.book-room').element_by(have.exact_text('Book'))

    def fill_firstname(self, firstname):
        self.firstname.type(firstname)
        return self

    def fill_lastname(self, lastname):
        self.lastname.type(lastname)
        return self

    def fill_email(self, email):
        self.email.type(email)
        return self

    def fill_phone(self, phone):
        self.phone.type(phone)
        return self

    def choose_dates(self):
        target = self.target_day
        self.start_day.perform(actions.click_hold_and_move(target))
        return self

    def book(self):
        self.book_button.click()
