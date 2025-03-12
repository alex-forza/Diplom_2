import allure
import requests
from data import Api, ExpectedResults, StaticData
from helpers import password_generator

class TestUnauthorizedCreateOrder:
    @allure.title('Создаем заказ без авторизации с ингредиентом')
    @allure.description('ОР: статус 200')
    def test_non_authorized_create_order_with_ingredients(self, return_random_ingredient):
        ingredients = {"ingredients": [return_random_ingredient]}
        create_order = requests.post(Api.post_create_order, ingredients)
        assert create_order.json()["success"] == True and create_order.status_code == 200

    @allure.title('Создаем заказ без авторизации и ингредиента')
    @allure.description('ОР: ошибка 400')
    def test_non_authorized_create_order_without_ingredients(self):
        ingredients = {"ingredients": []}
        create_order = requests.post(Api.post_create_order, ingredients)
        assert (create_order.json() == ExpectedResults.no_ingredient_error_400
                and create_order.status_code == 400)

    @allure.title('Создаем заказ без авторизации и неправильным хэшем')
    @allure.description('ОР: ошибка 500')
    def test_non_authorized_create_order_with_false_hash_ingredients(self):
        ingredients = {"ingredients": [password_generator()]}
        create_order = requests.post(Api.post_create_order, ingredients)
        assert create_order.status_code == 500

class TestLoginUserCreateOrder:
    @allure.title('Создаем заказ при авторизации с ингредиентом -> передаем токен')
    @allure.description('ОР: статус 200')
    def test_login_user_create_order_with_ingredients(self, return_random_ingredient):
        ingredients = {"ingredients": [return_random_ingredient]}
        response = requests.post(Api.post_login, data=StaticData.static_user_payload)
        auth_token = response.json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200
        create_order = requests.post(Api.post_create_order,
                                     headers={"authorization": f"{auth_token}"}, data=ingredients)
        assert create_order.json()["success"] == True and create_order.status_code == 200

    @allure.title('Создаем заказ если при авторизации с переданным токеном и без ингредиента')
    @allure.description('ОР: ошибка 400')
    def test_login_user_create_order_without_ingredients(self):
        ingredients = {"ingredients": []}
        response = requests.post(Api.post_login, data=StaticData.static_user_payload)
        auth_token = response.json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200
        create_order = requests.post(Api.post_create_order,
                                     headers={"authorization": f"{auth_token}"}, data=ingredients)
        assert (create_order.json() == ExpectedResults.no_ingredient_error_400
                and create_order.status_code == 400)

    @allure.title('Создаем заказ при авторизации, переданном токене и неправильном хэше ингредиента')
    @allure.description('ОР: ошибка 500')
    def test_login_user_create_order_with_false_hash_ingredients(self):
        ingredients = {"ingredients": [password_generator()]}
        response = requests.post(Api.post_login, data=StaticData.static_user_payload)
        auth_token = response.json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200
        create_order = requests.post(Api.post_create_order,
                                     headers={"authorization": f"{auth_token}"}, data=ingredients)
        assert create_order.status_code == 500