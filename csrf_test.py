import requests
import re

session = requests.Session()
for path in ['/accounts/signin/', '/accounts/signup/']:
    r = session.get('http://127.0.0.1:8000' + path, timeout=5)
    print('GET', path, r.status_code)
    token_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', r.text)
    print('TOKEN_FOUND', bool(token_match))
    if token_match:
        token = token_match.group(1)
        print('TOKEN', token[:12])
        if path == '/accounts/signup/':
            data = {
                'full_name': 'Test User',
                'email': 'test-email-1@example.com',
                'password': 'pass1234',
                'confirm_password': 'pass1234',
                'csrfmiddlewaretoken': token,
            }
            r2 = session.post('http://127.0.0.1:8000/accounts/signup/', data=data, timeout=5)
            print('POST SIGNUP', r2.status_code)
            print(r2.text[:300].replace('\n','\\n'))
    print('COOKIES', session.cookies.get_dict())
    print('---')
