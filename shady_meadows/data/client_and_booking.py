import dataclasses
from datetime import datetime, timedelta


def generate_booking_dates(date):
    start_date = datetime.today().replace(day=date)
    end_date = start_date + timedelta(days=1)
    return start_date, end_date

@dataclasses.dataclass
class Client:
    firstname: str
    lastname: str
    email: str
    phone: str
    subject: str
    message: str


client = Client(
    firstname='TestName',
    lastname='TestLastName',
    email='test@test.ru',
    phone='+7(911)123-45-67',
    subject='Super important subject',
    message='Super important message'
)