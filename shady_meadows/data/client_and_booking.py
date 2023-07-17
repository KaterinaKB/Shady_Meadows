import dataclasses
from datetime import datetime, timedelta

from faker import Faker

def create_random_firstname():
    fake = Faker()
    firstname = fake.first_name()
    return firstname

def create_random_lastname():
    fake = Faker()
    lastname = fake.last_name()
    return lastname

def create_random_email():
    fake = Faker()
    email = fake.email()
    return email


def create_random_phone():
    fake = Faker()
    phone = fake.phone_number()
    return phone

def create_random_text(max_count_of_symbols):
    fake = Faker()
    text = fake.text(max_nb_chars = max_count_of_symbols)
    return text


def create_booking_dates(date):
    fake = Faker()
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

@dataclasses.dataclass
class BookingDates:
    start_date: datetime.date
    end_date: datetime.date


client = Client(
    firstname=create_random_firstname(),
    lastname=create_random_lastname(),
    email=create_random_email(),
    phone=create_random_phone(),
    subject=create_random_text(20),
    message=create_random_text(200)
)


