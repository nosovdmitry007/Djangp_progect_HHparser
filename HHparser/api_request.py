import requests
import pprint
from .hhparser.kluch import token_my
# response = requests.get('http://127.0.0.1:8000/api/skills/', auth=('Dima', '1234'))

token = token_my()
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/skills/',  headers=headers)
pprint.pprint(response.json())