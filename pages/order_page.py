import allure
from api_connector import APIConnector
from constants import Url

class OrderApi:
    def __init__(self, api_connetor):
        self.api_connector = api_connetor

    @allure.step('Запрос на создание заказа методом POST')
    def create_order(self, data):
        return self.api_connector.post(Url.order, data=data)
    
    @allure.step('Запрос на получение заказа методом GET')
    def get_order(self, id_courier=None):
        get_params = {'courierID': id_courier} if id_courier is not None else {}
        return self.api_connector.get(Url.order, params=get_params)
    