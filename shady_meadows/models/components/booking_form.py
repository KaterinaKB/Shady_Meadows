from selene import browser, have, be
from shady_meadows.models.utils import actions
from shady_meadows.data import client_and_booking as data


class BookingForm:
    def __init__(self):
        self.firstname = browser.element("[name=firstname]")
        self.lastname = browser.element("[name=lastname]")
        self.email = browser.element("[name=email]")
        self.phone = browser.element("[name=phone]")
        self.date = browser.all("div[role=cell]:not(.rbc-off-range)")
        self.book_button = browser.all(".book-room").element_by(have.exact_text("Book"))
        self.confirmation_modal = browser.element(".confirmation-modal")
        self.dates_in_confirmation = self.confirmation_modal.element(
            "p:nth-child(even)"
        )
        self.close_button_on_confirmation_modal = self.confirmation_modal.element(
            "button"
        )
        self.error_message = browser.element('.alert.alert-danger')
        self.cancel_reservation = browser.all(".book-room").element_by(have.exact_text("Cancel"))

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

    def choose_dates(self, start_date, end_date):
        source_day = self.date.element_by(have.exact_text(start_date.strftime("%d")))
        target_day = self.date.element_by(have.exact_text(end_date.strftime("%d")))
        source_day.perform(actions.click_hold_and_move(target_day))
        return self

    def book(self):
        self.book_button.click()

    def check_if_confirmation_modal_is_visible(self):
        self.confirmation_modal.should(be.visible)

    def check_if_booking_dates_are_right(self, start_date, end_date):
        self.dates_in_confirmation.should(
            have.text(
                f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}"
            )
        )

    def close_confirmation_modal(self):
        self.close_button_on_confirmation_modal.click()

    def check_error_text(self, text):
        self.error_message.should(have.text(text))

    def check_total_price(self, duration):
        element = browser.element(f'[title="{duration} night(s) - £{duration * 100}"]')
        element.should(be.visible)