from shady_meadows.models.components.message_form import MessageForm
from shady_meadows.models.pages.admin_messages_page import AdminMessagesPage
from shady_meadows.models.pages.admin_page import AdminPage
from shady_meadows.models.pages.main_page import MainPage
from shady_meadows.data.client_and_booking import client
from project_config import project_config


class TestMessages:
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

    def test_receiving_message_by_admin(self):
        # GIVEN
        main_page = MainPage()
        message_form = MessageForm()
        admin_page = AdminPage()
        message_page = AdminMessagesPage()
        main_page.open()
        main_page.press_open_booking_button()
        (
            message_form.fill_name(client.firstname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .fill_subject(client.subject)
            .fill_message(client.message)
            .submit()
        )

        # WHEN
        admin_page.open()
        admin_page.login(project_config.admin_login, project_config.admin_pwd)
        admin_page.go_to_messages_page()

        # THEN
        message_page.check_if_certain_message_exists(client.firstname, client.subject)
        message_page.open_message(client.subject)
        message_page.check_content_of_message(
            client.firstname,
            client.email,
            client.phone,
            client.subject,
            client.message
        )



