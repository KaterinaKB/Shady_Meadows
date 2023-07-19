import allure
import pytest
from allure_commons.types import Severity

from shady_meadows.model.application import app
from shady_meadows.data.client_and_booking import client
from shady_meadows.data.client_and_booking import generate_booking_dates
from shady_meadows.data import errors as e


@allure.epic('Бронирование')
@allure.feature('Валидация полей формы бронирования')
class TestsValidationOfBookingForm:
    @allure.story('Валидация поля Имя')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'Voronova K.')
    @allure.title('Тест отображения ошибки "{expected_error}", используемое тестовое имя: "{firstname}"')
    @pytest.mark.parametrize(
        "firstname, expected_error",
        [
            ("", e.firstname_is_blank),
            ("Ed", e.wrong_size_of_firstname),
            ("Alexander Maximilian", e.wrong_size_of_firstname),
        ],
        ids=[
            "Blank firstname",
            "Too short firstname (2 symbols)",
            "Too long firstname (19 symbols)",
        ],
    )
    def test_validation_firstname_in_booking_form(self, firstname, expected_error):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()
        start_date, end_date = generate_booking_dates(27, 1)

        # WHEN
        (
            app.booking_form.fill_firstname(firstname)
            .fill_lastname(client.lastname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .choose_dates(start_date, end_date)
            .book()
        )
        # THEN
        app.booking_form.check_error_text(expected_error)

    @allure.story('Валидация поля Фамилия')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'Voronova K.')
    @allure.title('Тест отображения ошибки "{expected_error}", используемая тестовая фамилия: "{lastname}"')
    @pytest.mark.parametrize(
        "lastname, expected_error",
        [
            ("", e.lastname_is_blank),
            ("Le", e.wrong_size_of_lastname),
            ("los Remedios Cipriano Ruiz y Picasso", e.wrong_size_of_lastname),
        ],
        ids=[
            "Blank lastname",
            "Too short lastname (2 symbols)",
            "Too long lastname (31 symbols)",
        ],
    )
    def test_validation_lastname_in_booking_form(self, lastname, expected_error):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()
        start_date, end_date = generate_booking_dates(27, 1)

        # WHEN
        (
            app.booking_form.fill_firstname(client.firstname)
            .fill_lastname(lastname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .choose_dates(start_date, end_date)
            .book()
        )
        # THEN
        app.booking_form.check_error_text(expected_error)

    @allure.story('Валидация поля Электронная почта')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'Voronova K.')
    @allure.title('Тест отображения ошибки "{expected_error}", используемая тестовая э.почта: "{email}"')
    @pytest.mark.parametrize(
        "email, expected_error",
        [("", e.email_is_blank), ("test.ru", e.wrong_format_of_email)],
        ids=["Blank email", "Email without @"],
    )
    def test_validation_email_in_booking_form(self, email, expected_error):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()
        start_date, end_date = generate_booking_dates(27, 1)

        # WHEN
        (
            app.booking_form.fill_firstname(client.firstname)
            .fill_lastname(client.lastname)
            .fill_email(email)
            .fill_phone(client.phone)
            .choose_dates(start_date, end_date)
            .book()
        )
        # THEN
        app.booking_form.check_error_text(expected_error)

    @allure.story('Валидация поля Телефон')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'Voronova K.')
    @allure.title('Тест отображения ошибки "{expected_error}", используемый тестовый телефон: "{phone}"')
    @pytest.mark.parametrize(
        "phone, expected_error",
        [
            ("", e.phone_is_blank),
            ("1234567890", e.wrong_size_of_phone),
            ("+1234567890-1234567890", e.wrong_size_of_phone),
        ],
        ids=[
            "Blank phone",
            "Too short phone (10 symbols)",
            "Too long phone (22 symbols)",
        ],
    )
    def test_validation_phone_in_booking_form(self, phone, expected_error):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()
        start_date, end_date = generate_booking_dates(27, 1)

        # WHEN
        (
            app.booking_form.fill_firstname(client.firstname)
            .fill_lastname(client.lastname)
            .fill_email(client.email)
            .fill_phone(phone)
            .choose_dates(start_date, end_date)
            .book()
        )
        # THEN
        app.booking_form.check_error_text(expected_error)


    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'Voronova K.')
    @allure.title('Тест отображения ошибки при незаполненных датах бронирования')
    def test_validation_dates_in_booking_form(self):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()

        # WHEN
        (
            app.booking_form.fill_firstname(client.firstname)
            .fill_lastname(client.lastname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .book()
        )
        # THEN
        app.booking_form.check_error_text(e.dates_not_selected)
