import allure
import requests
from constants import Url

@allure.story('Проверка списка заказов')
class TestOrderList:
   @allure.title('Запрос возвращает код 200 и содержит orders')
   def test_list_orders(self):
      response = requests.get(f'{Url.host}{Url.order}')
      json_response = response.json()
      assert response.status_code == 200 and 'orders' in json_response.keys()