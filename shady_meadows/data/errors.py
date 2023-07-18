import random
import string

unavailable_dates = 'The room dates are either invalid or are already booked for one or more of the dates that you have selected.'
wrong_size_of_firstname = 'размер должен находиться в диапазоне от 3 до 18'
firstname_is_blank = 'Firstname should not be blank'
wrong_size_of_lastname = 'размер должен находиться в диапазоне от 3 до 30'
lastname_is_blank = 'Lastname should not be blank'
wrong_format_of_email = 'должно иметь формат адреса электронной почты'
email_is_blank = 'не должно быть пустым'
wrong_size_of_phone = 'размер должен находиться в диапазоне от 11 до 21'
phone_is_blank = 'не должно быть пустым'
dates_not_selected = 'не должно равняться null'


def generate_random_string(length):
    symbols = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(symbols) for i in range(length))
    return random_string
