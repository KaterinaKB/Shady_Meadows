import dataclasses
from datetime import datetime, timedelta


def generate_booking_dates(start_date, duration):
    start_date = datetime.today().replace(day=start_date)
    end_date = start_date + timedelta(days=duration)
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')


@dataclasses.dataclass
class Client:
    firstname: str
    lastname: str
    email: str
    phone: str
    subject: str
    message: str
    room: int


client = Client(
    firstname='TestName',
    lastname='TestLastname',
    email='test@test.ru',
    phone='+7(911)123-45-67',
    subject='Super important subject',
    message='Super important message',
    room=1
)