import requests
import pprint
from .hhparser.kluch import my_kluch
# response = requests.get('http://127.0.0.1:8000/api/skills/', auth=('Dima', '1234'))


headers = {'Authorization': f'Token {my_kluch()}'}
response = requests.get('http://127.0.0.1:8000/api/skills/',  headers=headers)
pprint.pprint(response.json())