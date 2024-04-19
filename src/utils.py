from pprint import pprint
import requests

params = {'query': 'python',
          'area': '1',
          'per_page': 10
          }

response = requests.get(url="https://api.hh.ru/vacancies", params=params)
pprint(response.json()['items'])