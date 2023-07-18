import pytest

from shady_meadows.models.components.booking_form import BookingForm
from shady_meadows.models.pages.main_page import MainPage
from shady_meadows.data.client_and_booking import client
from shady_meadows.data.client_and_booking import create_booking_dates
from shady_meadows.data import errors as e


@pytest.mark.parametrize(
    "firstname, expected_error",
    [
        (e.generate_random_string(0), e.firstname_is_blank),
        (e.generate_random_string(2), e.wrong_size_of_firstname),
        (e.generate_random_string(19), e.wrong_size_of_firstname)
    ]
)
def test_validation_firstname_in_booking_form(firstname, expected_error):
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = create_booking_dates(27)

    # WHEN
    (
        booking_form.fill_firstname(firstname)
        .fill_lastname(client.lastname)
        .fill_email(client.email)
        .fill_phone(client.phone)
        .choose_dates(start_date, end_date)
        .book()
    )
    # THEN
    booking_form.check_error_text(expected_error)


@pytest.mark.parametrize(
    "lastname, expected_error",
    [
        (e.generate_random_string(0), e.lastname_is_blank),
        (e.generate_random_string(2), e.wrong_size_of_lastname),
        (e.generate_random_string(31), e.wrong_size_of_lastname)
    ]
)
def test_validation_lastname_in_booking_form(lastname, expected_error):
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = create_booking_dates(27)

    # WHEN
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(lastname)
        .fill_email(client.email)
        .fill_phone(client.phone)
        .choose_dates(start_date, end_date)
        .book()
    )
    # THEN
    booking_form.check_error_text(expected_error)

@pytest.mark.parametrize(
    "email, expected_error",
    [
        (e.generate_random_string(0), e.email_is_blank),
        (e.generate_random_string(5), e.wrong_format_of_email)
    ]
)
def test_validation_email_in_booking_form(email, expected_error):
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = create_booking_dates(27)

    # WHEN
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(client.lastname)
        .fill_email(email)
        .fill_phone(client.phone)
        .choose_dates(start_date, end_date)
        .book()
    )
    # THEN
    booking_form.check_error_text(expected_error)

@pytest.mark.parametrize(
    "phone, expected_error",
    [
        (e.generate_random_string(0), e.phone_is_blank),
        (e.generate_random_string(10), e.wrong_size_of_phone),
        (e.generate_random_string(22), e.wrong_size_of_phone)
    ]
)
def test_validation_phone_in_booking_form(phone, expected_error):
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = create_booking_dates(27)

    # WHEN
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(client.lastname)
        .fill_email(client.email)
        .fill_phone(phone)
        .choose_dates(start_date, end_date)
        .book()
    )
    # THEN
    booking_form.check_error_text(expected_error)


def test_validation_dates_in_booking_form():
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()

    # WHEN
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(client.lastname)
        .fill_email(client.email)
        .fill_phone(client.phone)
        .book()
    )
    # THEN
    booking_form.check_error_text(e.dates_not_selected)