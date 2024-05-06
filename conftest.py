import pytest
from api_connector import APIConnector
from pages.courier_page import CourierApi
from pages.order_page import OrderApi

@pytest.fixture
def api_connector():
    return APIConnector()

@pytest.fixture
def courier_page(api_connector):
    return CourierApi(api_connector)

@pytest.fixture
def order_page(api_connector):
    return OrderApi(api_connector)