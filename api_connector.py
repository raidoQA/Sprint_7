import requests
from constants import Url

class APIConnector:
    def __init__(self):
        self.host = Url.host
    
    def post(self, order, data=None):
        url = f'{self.host}{order}'
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f'Ошибка запроса к{url}:{e}')
            return response
    
    def get(self, order, params=None):
        url = f'{self.host}{order}'
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f'Ошибка запроса к{url}:{e}')
            return response

    
        