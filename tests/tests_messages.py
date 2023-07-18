import pytest

from shady_meadows.models.components.message_form import MessageForm
from shady_meadows.models.pages.main_page import MainPage
from shady_meadows.data.client_and_booking import client
from shady_meadows.data.client_and_booking import generate_booking_dates
from shady_meadows.data import errors


class TestsMessages:
    def test_message_sending(self):
        # GIVEN
        main_page = MainPage()
        message_form = MessageForm()
        main_page.open()
        main_page.press_open_booking_button()

        # WHEN
        (
            message_form.fill_name(client.firstname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .fill_subject(client.subject)
            .fill_message(client.message)
            .submit()
        )

        # THEN
        message_form.check_reply_to_message(client.firstname, client.subject)