import allure
from constants import CourierName
from constants import NotRegCourier
from constants import WithoutName


@allure.story('Авторизация курьера')
class TestLoginCourier:
    @allure.title('Авторизация - Успешна')
    def test_autorize_login_success(self, courier_page):
        data_login = {'login': CourierName.login, 'password': CourierName.password}
        response = courier_page.login_courier(data=data_login)
        assert response.status_code == 200
        assert 'id' in response.json()


    @allure.title('Попытка авторизации под незарегистрированным курьером')
    def test_not_reg_courier(self, courier_page):
        data_login = {'login': NotRegCourier.login, 'password':NotRegCourier.password}
        response = courier_page.login_courier(data=data_login)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'


    @allure.title('Попытка авторизации без логина')
    def test_autorize_without_login(self, courier_page):
        data_login = {'login': WithoutName.login, 'password': WithoutName.password}
        response = courier_page.login_courier(data=data_login)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Попытка авторизации без логина и пароля')
    def test_autorize_without_login_and_password(self, courier_page):
        data_login = {'login': WithoutName.login, 'password': WithoutName.null_password}
        response = courier_page.login_courier(data=data_login)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'