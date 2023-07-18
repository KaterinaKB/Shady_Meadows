from shady_meadows.models.components.booking_form import BookingForm
from shady_meadows.models.pages.main_page import MainPage
from shady_meadows.data.client_and_booking import client
from shady_meadows.data.client_and_booking import generate_booking_dates
from shady_meadows.data import errors


def test_booking_creation():
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = generate_booking_dates(1)

    # WHEN
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(client.lastname)
        .fill_email(client.email)
        .fill_phone(client.phone)
        .choose_dates(start_date, end_date)
        .book()
    )
    # THEN
    booking_form.check_if_confirmation_modal_is_visible()


def test_confirmation_data_after_booking():
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = generate_booking_dates(3)

    # WHEN
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(client.lastname)
        .fill_email(client.email)
        .fill_phone(client.phone)
        .choose_dates(start_date, end_date)
        .book()
    )
    # THEN
    booking_form.check_if_booking_dates_are_right(start_date, end_date)


def test_if_registration_is_not_possible_on_an_unavailable_day():
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = generate_booking_dates(5)
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(client.lastname)
        .fill_email(client.email)
        .fill_phone(client.phone)
        .choose_dates(start_date, end_date)
        .book()
    )
    booking_form.close_confirmation_modal()
    main_page.press_open_booking_button()

    # WHEN
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(client.lastname)
        .fill_email(client.email)
        .fill_phone(client.phone)
        .choose_dates(start_date, end_date)
        .book()
    )

    # THEN
    booking_form.check_error_text(errors.unavailable_dates)


def test_total_price_of_a_reservation():
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = generate_booking_dates(5)
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(client.lastname)
        .fill_email(client.email)
        .fill_phone(client.phone)
        .choose_dates(start_date, end_date)
        .book()
    )
    booking_form.close_confirmation_modal()
    main_page.press_open_booking_button()

    # WHEN
    (
        booking_form.fill_firstname(client.firstname)
        .fill_lastname(client.lastname)
        .fill_email(client.email)
        .fill_phone(client.phone)
        .choose_dates(start_date, end_date)
        .book()
    )

    # THEN
    booking_form.check_error_text(errors.unavailable_dates)