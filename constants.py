class Url:
    #url
    host = 'http://qa-scooter.praktikum-services.ru'

    #Courier
    login_courier = '/api/v1/courier/login'
    create_courier = '/api/v1/courier'

    #Orders
    order = '/api/v1/orders'


class CourierName:
    login = 'CourierTester1016'
    password = 'passwdZXCgoul'
    first_name = 'Тестерович'

class NotRegCourier:
    login = 'CourierTester9990'
    password = 'fdfdffvvv'

class WithoutName:
    login = ''
    password = 'vervegf34'
    null_password = ''

class DataForOrder:
    order_data = {
        'firstName': 'Андрей',
        'lastName:': 'Тестерович',
        'address': 'Мск',
        'metroStation': '3',
        'phone': '+79991234567',
        'rentTime': '3',
        'deliveryDate': '2024-05-10',
        'comment': 'hello, friend',
    }
