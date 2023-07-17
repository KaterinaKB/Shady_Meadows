import requests


def test_get_booking():
    response = requests.get('https://restful-booker.herokuapp.com/booking')

    print(response.json())
    print(len(response.json()))


def test_get_booking_by_name():
    response = requests.get('https://restful-booker.herokuapp.com/booking?firstname=Kate')

    print(response.json())


def test_get_booking_by_checkin():
    response = requests.get('https://restful-booker.herokuapp.com/booking?checkin=2023-07-30')

    print(response.json())


def test_get_booking_by_id():
    response = requests.get('https://automationintesting.online/booking')

    print(response.json())


def test_create_token():
    response = requests.post(
        url='https://restful-booker.herokuapp.com/auth',
        json={
            "username": 'admin',
            "password": 'password123'}
    )

    print(response.json())

def test_create_booking():
    response = requests.post(
        url='https://automationintesting.online/booking',
        json={
            "firstname": 'Kate',
            "lastname": 'TestKate',
            "totalprice": '123',
            "depositpaid": 'true',
            "roomid": 1,
            "bookingdates": {
                "checkin": '2023-07-30',
                "checkout": '2023-08-01',
            },
            "additionalneeds": 'password123'}
    )

    print(response.json())