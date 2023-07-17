from shady_meadows.models.components.booking_form import BookingForm
from shady_meadows.models.pages.main_page import MainPage
from shady_meadows.data.client_and_booking import client
from shady_meadows.data.client_and_booking import create_booking_dates


def test_create_booking():
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = create_booking_dates(1)

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


def test_check_confirmation_data_after_booking():
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = create_booking_dates(3)

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


def test_check_unavailable_spots_after_booking():
    # GIVEN
    main_page = MainPage()
    booking_form = BookingForm()
    main_page.open()
    main_page.press_open_booking_button()
    start_date, end_date = create_booking_dates(25)

    #WHEN
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

    # THEN
    booking_form.check_unavailable_status_in_calendar(start_date, end_date)
