import pytest
from shady_meadows.model.application import app
from shady_meadows.data.client_and_booking import client
from shady_meadows.data.client_and_booking import generate_booking_dates
from shady_meadows.data import errors


class TestsBooking:
    @pytest.mark.parametrize("duration", [1, 12], ids=["One night", "Twelve nights"])
    def test_total_price_of_a_reservation(self, duration):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()

        # WHEN
        start_date, end_date = generate_booking_dates(1, duration)
        app.booking_form.choose_dates(start_date, end_date)

        # THEN
        app.booking_form.check_total_price(duration)

    def test_booking_creation(self):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()
        start_date, end_date = generate_booking_dates(1, 1)

        # WHEN
        (
            app.booking_form.fill_firstname(client.firstname)
            .fill_lastname(client.lastname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .choose_dates(start_date, end_date)
            .book()
        )
        # THEN
        app.booking_form.check_if_confirmation_modal_is_visible()

    def test_confirmation_data_after_booking(self):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()
        start_date, end_date = generate_booking_dates(3, 1)

        # WHEN
        (
            app.booking_form.fill_firstname(client.firstname)
            .fill_lastname(client.lastname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .choose_dates(start_date, end_date)
            .book()
        )
        # THEN
        app.booking_form.check_if_booking_dates_are_right(start_date, end_date)

    def test_if_registration_is_not_possible_on_an_unavailable_day(self):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()
        start_date, end_date = generate_booking_dates(5, 1)
        (
            app.booking_form.fill_firstname(client.firstname)
            .fill_lastname(client.lastname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .choose_dates(start_date, end_date)
            .book()
        )
        app.booking_form.close_confirmation_modal()
        app.main_page.press_open_booking_button()

        # WHEN
        (
            app.booking_form.fill_firstname(client.firstname)
            .fill_lastname(client.lastname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .choose_dates(start_date, end_date)
            .book()
        )

        # THEN
        app.booking_form.check_error_text(errors.unavailable_dates)