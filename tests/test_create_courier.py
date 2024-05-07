import allure
from data import Messages

@allure.story('Создаем курьера')
class TestCreateCourier:
    @allure.title('Проверка на создание курьера с обязательными данными')
    def test_create_courier(self, courier_page):
        data_courier = courier_page.valid_data_courier()
        response = courier_page.create_courier(data_courier)
        assert response.status_code == 201
        assert response.json() == Messages.courier_created

    @allure.title('Проверка на создание курьера с одинаковыми данными')
    def test_create_duplicate_courier(self, courier_page):
        data_courier = courier_page.valid_data_courier()
        courier_page.create_courier(data_courier)
        response = courier_page.create_courier(data_courier)
        assert response.status_code == 409
        assert response.json()['message'] == Messages.duplicate_courier

    @allure.title('Проверка на создание курьера с неполными данными')
    def test_create_courier_without_any_field(self, courier_page):
        data_courier = courier_page.valid_data_courier()
        del data_courier['password']
        response = courier_page.create_courier(data_courier)
        assert response.status_code == 400
        assert response.json()['message'] == Messages.incomplete_data