import allure
import requests
from data import Api, StaticData, ExpectedResults
from helpers import mail_generator, password_generator

class TestLoginUser:
    @allure.title('Логин существующим пользователем.')
    @allure.description('ОР: статус 200, accessToken в ответе')
    def test_post_login_user_true(self):
        response = requests.post(Api.post_login, data=StaticData.static_user_payload)
        assert "accessToken" in response.json() and response.status_code == 200

    @allure.title('Попытка логика под несуществующим пользователем')
    @allure.description('ОР: статус 401')
    def test_unauthorized_user(self):
        payload = {
            "email": mail_generator(),
            "password": password_generator()
        }
        response = requests.post(Api.post_login, data=payload)
        assert response.json() == ExpectedResults.error_403_unauthorized and response.status_code == 401