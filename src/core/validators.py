import re


def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))


def validate_phone(phone):
    phone_pattern = r'^\+\d{1,2}\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
    return bool(re.match(phone_pattern, phone))


def validate_date(date):
    date_pattern = r'^(?:\d{2}\.\d{2}.\d{4}|\d{4}-\d{2}-\d{2})$'
    return bool(re.match(date_pattern, date))
