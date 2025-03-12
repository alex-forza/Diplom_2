import random

def mail_generator():
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    name = ''.join(random.choice(letters) for i in range(10))
    domain = ''.join(random.choice(letters) for i in range(6))
    country = ['ru', 'com']
    mail = f'{name}@{domain}.{random.choice(country)}'
    return mail

def password_generator():
    symbols = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    password = ''.join(random.choice(symbols) for i in range(0, 10))
    return password

def name_generator():
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    frs_name = ''.join(random.choice(letters) for i in range(10))
    lst_name = ''.join(random.choice(letters) for i in range(10))
    return f"{frs_name} {lst_name}"

def payload_new_user():
    new_user = {
        "email": mail_generator(),
        "password": password_generator(),
        "name": name_generator()
        }
    return new_user