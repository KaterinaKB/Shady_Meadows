import allure
import pytest
from allure_commons.types import Severity

from shady_meadows.model.application import app
from shady_meadows.data.client_and_booking import client
from shady_meadows.data.client_and_booking import generate_booking_dates
from shady_meadows.data import errors as e


@allure.epic("Booking")
@allure.feature("Booking Form Field Validation")
@allure.label("owner", "Voronova K.")
class TestsValidationOfBookingForm:
    @allure.story("Firstname field validation")
    @allure.severity(Severity.NORMAL)
    @allure.title(
        'Test for display error: "{expected_error}", test name used: "{firstname}"'
    )
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
    def test_validation_firstname_in_booking_form(
        self, setup_browser, firstname, expected_error
    ):
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

    @allure.story("Lastname field validation")
    @allure.severity(Severity.NORMAL)
    @allure.title(
        'Test for display error: "{expected_error}", test lastname used: "{lastname}"'
    )
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
    def test_validation_lastname_in_booking_form(
        self, setup_browser, lastname, expected_error
    ):
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

    @allure.story("Email field validation")
    @allure.severity(Severity.NORMAL)
    @allure.title(
        'Test for display error: "{expected_error}", test email used: "{email}"'
    )
    @pytest.mark.parametrize(
        "email, expected_error",
        [("", e.email_is_blank), ("test.ru", e.wrong_format_of_email)],
        ids=["Blank email", "Email without @"],
    )
    def test_validation_email_in_booking_form(
        self, setup_browser, email, expected_error
    ):
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

    @allure.story("Phone field validation")
    @allure.severity(Severity.NORMAL)
    @allure.title(
        'Test for display error: "{expected_error}", test phone used: "{phone}"'
    )
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
    def test_validation_phone_in_booking_form(
        self, setup_browser, phone, expected_error
    ):
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
    @allure.title("Test for error display in case of blank booking dates")
    def test_validation_dates_in_booking_form(self, setup_browser):
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
