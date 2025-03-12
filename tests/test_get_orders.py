import allure
import requests
from data import Api, StaticData, ExpectedResults

class TestGetOrders:
    @allure.title('Получаем все заказы в системе без авторизации (50 шт. последних)')
    @allure.description('ОР: статус 200')
    def test_get_all_orders(self):
        response = requests.get(Api.get_all_orders)
        assert response.json()["success"] == True and response.status_code == 200
        assert "total" and "totalToday" in response.json()

    @allure.title('Попытка получение заказа без авторизации')
    @allure.description('ОР: ошибка 401')
    def test_non_authorized_get_orders(self):
        response = requests.get(Api.get_order)
        assert (response.json() == ExpectedResults.error_401_unauthorized_user
                and response.status_code == 401)

    @allure.title('Авторизуемся и получаем заказы пользователя.')
    @allure.description('ОР: статус 200')
    def test_get_orders_login(self):
        response = requests.post(Api.post_login, data=StaticData.static_user_payload)
        auth_token = response.json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200
        order_info = requests.get(Api.get_order,  headers={"authorization": f"{auth_token}"})
        assert order_info.json()["success"] == True and order_info.status_code == 200
        assert "total" and "totalToday" in order_info.json()