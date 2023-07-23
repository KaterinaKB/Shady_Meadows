import allure
import requests
from allure_commons._allure import step
from allure_commons.types import Severity
from jsonschema.validators import validate
from shady_meadows.data.client_and_booking import client, generate_booking_dates
from shady_meadows.model.application import app
from shady_meadows.utils.load_json_schema import load_json_schema


@allure.epic('Booking')
@allure.feature('API')
@allure.label('owner', 'Voronova K.')
class TestBookingAPI:

    @allure.severity(Severity.BLOCKER)
    @allure.title('Test for status code in booking creation response')
    def test_create_booking_returns_200(self):
        # WHEN
        with step("Generate booking dates"):
            start_date, end_date = generate_booking_dates(10, 3)
        with step(f"Create reservation since {start_date} to {end_date}"):
            response = requests.post(
                url=f"{app.api.base_url}/booking/",
                json={
                    "bookingid": 0,
                    "roomid": client.room,
                    "firstname": client.firstname,
                    "lastname": client.lastname,
                    "depositpaid": "true",
                    "email": client.email,
                    "phone": client.phone,
                    "bookingdates": {"checkin": start_date, "checkout": end_date},
                },
            )

        # THEN
        with step("Check if status code is 201"):
            assert response.status_code == 201

        app.api.find_booking_id_and_delete_booking(client)

    @allure.severity(Severity.CRITICAL)
    @allure.title('Test for booking info in booking creation response')
    def test_create_booking_returns_right_booking_info(self):
        # WHEN
        with step("Generate booking dates"):
            start_date, end_date = generate_booking_dates(10, 3)
        with step(f"Create reservation since {start_date} to {end_date}"):
            response = requests.post(
                url=f"{app.api.base_url}/booking/",
                json={
                    "bookingid": 0,
                    "roomid": client.room,
                    "firstname": client.firstname,
                    "lastname": client.lastname,
                    "depositpaid": "true",
                    "email": client.email,
                    "phone": client.phone,
                    "bookingdates": {"checkin": start_date, "checkout": end_date},
                },
            )

        # THEN
        with step("Check information about booking"):
            booking_info = response.json()["booking"]
            assert (
                booking_info["bookingid"] > 0
                and booking_info["roomid"] == client.room
                and booking_info["firstname"] == client.firstname
                and booking_info["lastname"] == client.lastname
                and booking_info["bookingdates"]["checkin"] == start_date
                and booking_info["bookingdates"]["checkout"] == end_date
            )

        app.api.find_booking_id_and_delete_booking(client)

    @allure.severity(Severity.BLOCKER)
    @allure.title('Test for schema of booking creation response')
    def test_create_booking_schema_validation(self):
        # WHEN
        with step("Generate booking dates"):
            start_date, end_date = generate_booking_dates(10, 3)
        with step(f"Create reservation since {start_date} to {end_date}"):
            response = requests.post(
                url=f"{app.api.base_url}/booking/",
                json={
                    "bookingid": 0,
                    "roomid": client.room,
                    "firstname": client.firstname,
                    "lastname": client.lastname,
                    "depositpaid": "true",
                    "email": client.email,
                    "phone": client.phone,
                    "bookingdates": {"checkin": start_date, "checkout": end_date},
                },
            )

        # THEN
        with step("Validate schema in response"):
            schema = load_json_schema("new_booking_response.json")
            validate(instance=response.json(), schema=schema)

        app.api.find_booking_id_and_delete_booking(client)

    @allure.severity(Severity.CRITICAL)
    @allure.title('Check status code in information about booking response')
    def test_get_information_about_booking_returns_200(self):
        # GIVEN
        with step("Generate booking dates"):
            start_date, end_date = generate_booking_dates(10, 3)
        app.api.create_booking(start_date, end_date, client)

        # WHEN
        app.api.login_as_admin()
        with step("Get booking information"):
            response = requests.get(
                url=f"{app.api.base_url}/booking/{app.api.booking_id}",
                cookies={"token": app.api.authorization_cookie},
            )

        # THEN
        with step("Check if status code is 200"):
            assert response.status_code == 200

        app.api.find_booking_id_and_delete_booking(client)

    @allure.severity(Severity.BLOCKER)
    @allure.title('Check status code in booking removal response')
    def test_delete_reservation_returns_202(self):
        # GIVEN
        with step("Generate booking dates"):
            start_date, end_date = generate_booking_dates(10, 3)
        app.api.create_booking(start_date, end_date, client)

        # WHEN
        app.api.login_as_admin()
        with step("Delete reservation"):
            response = requests.delete(
                url=f"{app.api.base_url}/booking/{app.api.booking_id}",
                cookies={"token": app.api.authorization_cookie},
            )

        # THEN
        with step("Check if status code is 202"):
            assert response.status_code == 202
