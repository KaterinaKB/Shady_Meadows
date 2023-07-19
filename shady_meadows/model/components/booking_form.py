import allure
from selene import browser, have, be
from shady_meadows.model.utils import actions


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

    @allure.step('Вводим имя {firstname}')
    def fill_firstname(self, firstname):
        self.firstname.type(firstname)
        return self

    @allure.step('Вводим фамилию {lastname}')
    def fill_lastname(self, lastname):
        self.lastname.type(lastname)
        return self

    @allure.step('Вводим адрес электронной почты {email}')
    def fill_email(self, email):
        self.email.type(email)
        return self

    @allure.step('Вводим номер телефона {phone}')
    def fill_phone(self, phone):
        self.phone.type(phone)
        return self

    @allure.step('Выбираем даты бронирования: с {start_date} по {end_date}')
    def choose_dates(self, start_date, end_date):
        source_day = self.date.element_by(have.exact_text(start_date.strftime("%d")))
        target_day = self.date.element_by(have.exact_text(end_date.strftime("%d")))
        source_day.perform(actions.click_hold_and_move(target_day))
        return self

    @allure.step('Бронируем')
    def book(self):
        self.book_button.click()

    @allure.step('Проверяем наличие подтверждения')
    def check_if_confirmation_modal_is_visible(self):
        self.confirmation_modal.should(be.visible)

    @allure.step('Проверяем корректность дат в подтверждении: с {start_date} по {end_date}')
    def check_if_booking_dates_are_right(self, start_date, end_date):
        self.dates_in_confirmation.should(
            have.text(
                f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}"
            )
        )

    @allure.step('Закрываем окно подтверждения')
    def close_confirmation_modal(self):
        self.close_button_on_confirmation_modal.click()

    @allure.step('Проверяем текст ошибки. Ожидаемый текст: {text}')
    def check_error_text(self, text):
        self.error_message.should(have.text(text))

    @allure.step('Проверяем стоимость бронирования за {duration} ночей')
    def check_total_price(self, duration):
        element = browser.element(f'[title="{duration} night(s) - £{duration * 100}"]')
        element.should(be.visible)