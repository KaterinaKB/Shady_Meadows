import requests


# def test_get_booking():
#     response = requests.get('https://restful-booker.herokuapp.com/booking')
#
#     print(response.json())
#     print(len(response.json()))
#
#
# def test_get_booking_by_name():
#     response = requests.get('https://restful-booker.herokuapp.com/booking?firstname=Kate')
#
#     print(response.json())
#
#
# def test_get_booking_by_checkin():
#     response = requests.get('https://restful-booker.herokuapp.com/booking?checkin=2023-07-30')
#
#     print(response.json())
#
#
# def test_get_booking_by_id():
#     response = requests.get('https://automationintesting.online/booking')
#
#     print(response.json())
#
# def test_create_token0():
#     response = requests.post(
#         url='https://restful-booker.herokuapp.com/auth',
#         json={
#             "username": "admin",
#             "password": "password123"
#         }
#     )
#
#     print(response.json())
#
def test_create_token():
    response = requests.post(
        url='https://automationintesting.online/auth/login',
        json={
            "username": "admin",
            "password": "password"
        }
    )

    print(response.cookies.get('token'))

def test_validate_token():
    response = requests.post(
        url='https://automationintesting.online/auth/validate',
        json={
            "token": "VOigDzWilBLi2MMe"
        }
    )
    print(response.status_code)



def test_create_booking():
    response = requests.post(
        url='https://automationintesting.online/booking/',
        json={
            "bookingid": 1,
            "roomid": 1,
            "firstname": "TestName",
            "lastname": "TestLastname",
            "depositpaid": "true",
            "email": "test@test.ru",
            "phone": "12345678901",
            "bookingdates": {
                "checkin": "2023-08-21",
                "checkout": "2023-08-23"
            }
        }
    )
    bookingid = response.json()['bookingid']
    print(bookingid)
    print(response.json())

    response2 = requests.get(
        url=f'https://automationintesting.online/booking/{bookingid}', cookies={"token": "VOigDzWilBLi2MMe"}
    )
    print(response2)




def test_get_summary():
    response = requests.get(
        url='https://automationintesting.online/booking/summary',
        params={'roomid': "1"}
    )

    print(response.json())

def test_get_information_about_booking():
        response = requests.get(
            url=f'https://automationintesting.online/booking/10', cookies={"token": "VOigDzWilBLi2MMe"}
        )

        print(response.json())


def test_get_room_id():
    response = requests.get(
        url=f'https://automationintesting.online/booking/', cookies={"token": "VOigDzWilBLi2MMe"}, params={'roomid': 1}
    )

    print(response.json())

def test_get_health():
        response = requests.get(
            url='https://automationintesting.online/auth/actuator/health'
        )

        print(response.json())
