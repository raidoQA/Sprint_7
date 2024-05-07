import allure
import pytest


@allure.story('Создание заказа')
class TestCreateOrder:
    @pytest.mark.parametrize('colors', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    @allure.title('Создание заказа с выбором цвета: {colors}')
    def test_create_order_success(self, order_page, colors):
        order_data = {
            'firstName': 'Андрей',
            'lastName:': 'Тестерович',
            'address': 'Мск',
            'metroStation': '3',
            'phoneNumber': '+79991234567',
            'rentTime': '3',
            'deliveryDate': '2024-05-10',
            'comment': 'hello, friend',
            "color": colors
        }
        response = order_page.create_order(order_data)
        assert response.status_code == 201
        assert "track" in response.json()