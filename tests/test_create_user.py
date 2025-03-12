import allure
import requests
import helpers
from data import Api, StaticData, ExpectedResults

class TestCreateUser:
    @allure.title('Создаём и удаляем пользователя.')
    @allure.description('ОР: при наличии accessToken - подтверждение создания')
    def test_create_and_delete_user(self):
        response = requests.post(Api.post_reg, data=helpers.payload_new_user())
        auth_token = requests.post(Api.post_reg, data=helpers.payload_new_user()).json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200
        del_user = requests.delete(Api.del_data, headers={"authorization": f"{auth_token}"})
        assert del_user.json() == ExpectedResults.delete_202 and del_user.status_code == 202

    @allure.title('Создание двух одинаковых пользователей. Передача существующего эмэйла')
    @allure.description('ОР: ошибка 403')
    def test_create_the_same_user(self):
        payload = {
            "email": StaticData.static_user_email,
            "password": helpers.password_generator(),
            "name": helpers.name_generator()
        }
        response = requests.post(Api.post_reg, data=payload)
        assert response.json() == ExpectedResults.error_403_exists and response.status_code == 403

    @allure.title('Создание пользователя без Email"а.')
    @allure.description('ОР: ошибка 403')
    def test_create_without_email(self):
        payload = {
        "email": "",
        "password": helpers.password_generator(),
        "name": helpers.name_generator()
        }
        response = requests.post(Api.post_reg, data=payload)
        assert response.json() == ExpectedResults.error_403_no_required_fields and response.status_code == 403

    @allure.title('Создание пользователя без Password"а')
    @allure.description('ОР: ошибка 403')
    def test_create_without_password(self):
        payload = {
            "email": helpers.mail_generator(),
            "password": "",
            "name": helpers.name_generator()
        }
        response = requests.post(Api.post_reg, data=payload)
        assert response.json() == ExpectedResults.error_403_no_required_fields and response.status_code == 403

    @allure.title('Создание пользователя без Name.')
    @allure.description('ОР: ошибка 403')
    def test_create_without_name(self):
        payload = {
            "email": helpers.mail_generator(),
            "password": helpers.password_generator(),
            "name": ""
        }
        response = requests.post(Api.post_reg, data=payload)
        assert response.json() == ExpectedResults.error_403_no_required_fields and response.status_code == 403

    @allure.title('Создание пользователя без !всех! полей.')
    @allure.description('ОР: ошибка 403')
    def test_create_without_all_field(self):
        payload = {
            "email": "",
            "password": "",
            "name": ""
        }
        response = requests.post(Api.post_reg, data=payload)
        assert response.json() == ExpectedResults.error_403_no_required_fields and response.status_code == 403