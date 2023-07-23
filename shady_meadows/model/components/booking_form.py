import allure
from selene import browser, have, be

from shady_meadows.data.client_and_booking import Client
from shady_meadows.utils import actions


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
        self.error_message = browser.element(".alert.alert-danger")
        self.cancel_reservation = browser.all(".book-room").element_by(
            have.exact_text("Cancel")
        )

    @allure.step("Enter a firstname {firstname}")
    def fill_firstname(self, firstname):
        self.firstname.type(firstname)
        return self

    @allure.step("Enter a lastname {lastname}")
    def fill_lastname(self, lastname):
        self.lastname.type(lastname)
        return self

    @allure.step("Enter an email {email}")
    def fill_email(self, email):
        self.email.type(email)
        return self

    @allure.step("Enter a phone {phone}")
    def fill_phone(self, phone):
        self.phone.type(phone)
        return self

    @allure.step("Choose booking dates: с {start_date} по {end_date}")
    def choose_dates(self, start_date, end_date):
        source_day = self.date.element_by(have.exact_text(start_date[8:]))
        target_day = self.date.element_by(have.exact_text(end_date[8:]))
        source_day.perform(actions.click_hold_and_move(target_day))
        return self

    @allure.step("Book")
    def book(self):
        self.book_button.click()

    @allure.step("Create booking")
    def create_booking(self, start_date, end_date, client=Client):
        (
            self.fill_firstname(client.firstname)
            .fill_lastname(client.lastname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .choose_dates(start_date, end_date)
            .book()
        )

    @allure.step("Check confirmation display")
    def check_if_confirmation_modal_is_visible(self):
        self.confirmation_modal.should(be.visible)

    @allure.step(
        "Check dates in confirmation, expect: since {start_date} till {end_date}"
    )
    def check_if_booking_dates_are_right(self, start_date, end_date):
        self.dates_in_confirmation.should(have.text(f"{start_date} - {end_date}"))

    @allure.step("Close the confirmation")
    def close_confirmation_modal(self):
        self.close_button_on_confirmation_modal.click()

    @allure.step("Check the text of the error. Expect: {text}")
    def check_error_text(self, text):
        self.error_message.should(have.text(text))

    @allure.step("Check the total cost of booking for {duration} nights")
    def check_total_price(self, duration):
        element = browser.element(f'[title="{duration} night(s) - £{duration * 100}"]')
        element.should(be.visible)
