import allure
from allure_commons.types import Severity

from shady_meadows.model.application import app
from shady_meadows.data.client_and_booking import client
from project_config import project_config


@allure.epic('Сообщения')
@allure.feature('Отправка сообщения')
class TestsMessages:

    @allure.severity(Severity.BLOCKER)
    @allure.label('owner', 'Voronova K.')
    @allure.title('Тест отправки сообщения в администрацию отеля')
    def test_message_sending(self):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()

        # WHEN
        (
            app.message_form.fill_name(client.firstname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .fill_subject(client.subject)
            .fill_message(client.message)
            .submit()
        )

        # THEN
        app.message_form.check_reply_to_message(client.firstname, client.subject)

    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Voronova K.')
    @allure.title('Тест корректности содержимого сообщения от клиента на странице администратора')
    def test_receiving_message_by_admin(self):
        # GIVEN
        app.main_page.open()
        app.main_page.press_open_booking_button()
        (
            app.message_form.fill_name(client.firstname)
            .fill_email(client.email)
            .fill_phone(client.phone)
            .fill_subject(client.subject)
            .fill_message(client.message)
            .submit()
        )

        # WHEN
        app.admin_page.open()
        app.admin_page.login(project_config.admin_login, project_config.admin_pwd)
        app.admin_page.go_to_messages_page()

        # THEN
        app.admin_message_page.check_if_certain_message_exists(
            client.firstname, client.subject
        )
        app.admin_message_page.open_message(client.subject)
        app.admin_message_page.check_content_of_message(
            client.firstname, client.email, client.phone, client.subject, client.message
        )
