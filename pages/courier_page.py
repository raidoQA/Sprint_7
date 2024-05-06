import allure
from constants import Url
from constants import CourierName

class CourierApi:
    def __init__(self, api_connector):
        self.api_connector = api_connector
        self.courier_id = None

    @allure.step('Создание курьера')
    def create_courier(self, data):
        return self.api_connector.post(Url.create_courier, data=data)
    
    @allure.step('Авторизация курьера')
    def login_courier(self, data):
        response = self.api_connector.post(Url.login_courier, data=data)
        if response.status_code == 200:
            self.courier_id = response.json().get('id')
        return response
    
    @allure.step('Ввод валидных данных курьера')
    def valid_data_courier(self):
        return{'login':CourierName.login, 'password':CourierName.password, 'firstName': CourierName.first_name}
    
    @allure.step('Извлечение идентификатора курьера')
    def get_courier_id(self):
        return self.get_courier_id