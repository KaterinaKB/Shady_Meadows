import allure
import requests

from project_config import project_config
from shady_meadows.data.client_and_booking import Client
from shady_meadows.utils.CustomSession import CustomSession


class ShadowMeadowsAPI:
    def __init__(self):
        self.session = CustomSession("https://automationintesting.online")
        self.authorization_cookie = None
        self.booking_id = None

    @allure.step('Login as admin')
    def login_as_admin(self):
        response = self.session.post(
            url="/auth/login",
            json={
                "username": project_config.admin_login,
                "password": project_config.admin_pwd
            }
        )

        self.authorization_cookie = response.cookies.get("token")
        return response

    @allure.step('Find booking id by client information')
    def find_booking_id_by_client(self, client = Client):
        response = self.session.get(
            url='/booking/', cookies={"token": self.authorization_cookie},
            params={'roomid': client.room}
        )

        for i in range(len(response.json()['bookings'])):
            if response.json()['bookings'][i]['firstname'] == client.firstname and response.json()['bookings'][i]['lastname'] == client.lastname:
                self.booking_id = response.json()['bookings'][i]['bookingid']
        return self.booking_id

    @allure.step('Create booking since {start_date} till {end_date}')
    def create_booking(self, start_date, end_date, client=Client):
        response = self.session.post(
            url='/booking/',
            json={
                "bookingid": 0,
                "roomid": client.room,
                "firstname": client.firstname,
                "lastname": client.lastname,
                "depositpaid": "true",
                "email": client.email,
                "phone": client.phone,
                "bookingdates": {
                    "checkin": start_date,
                    "checkout": end_date
                }
            }
        )
        self.booking_id = response.json()['bookingid']
        return response

    @allure.step('Delete booking')
    def delete_booking(self):
        self.session.delete(
            url=f'/booking/{self.booking_id}', cookies={"token": self.authorization_cookie}
        )

    @allure.step('POSTCONDITION: find booking id and delete booking')
    def find_booking_id_and_delete_booking(self, client=Client):
        self.login_as_admin()
        self.find_booking_id_by_client(client)
        self.delete_booking()


