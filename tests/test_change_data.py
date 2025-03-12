import allure
import requests
from data import Api, ExpectedResults
from helpers import mail_generator, name_generator, payload_new_user, password_generator

class TestChangeData:
    @allure.title('Пробуем изменить данные пользователя с неверным токеном')
    @allure.description('ОР: Ошибка 403')
    def test_change_data_with_false_token(self):
        auth_token = "Bearer blablabla"
        patch_email = {"email": mail_generator()}
        change_profile_data = requests.patch(Api.patch_change_data,
                                             headers={"authorization": auth_token}, data=patch_email)
        assert (change_profile_data.json() == ExpectedResults.error_403_token_bad_change_data
                and change_profile_data.status_code == 403)

    @allure.title('Меняем данные не авторизовавшись без передачи токена')
    @allure.description('ОР: Ошибка 401')
    def test_non_authorized_change_data(self):
        patch_email = {"email": mail_generator()}
        change_profile_data = requests.patch(Api.patch_change_data,
                                             headers={"authorization": ""}, data=patch_email)
        assert (change_profile_data.json() == ExpectedResults.error_401_unauthorized_user
                and change_profile_data.status_code == 401)

    @allure.title('Создаем -> логинимся -> изменяем имя пользователя -> удаляем пользователя')
    @allure.description('ОР: статусы 200 и 202')
    def test_change_profile_name(self):
        patch_name = {"name": name_generator()}
        new_user = requests.post(Api.post_reg, data=payload_new_user())
        auth_token = new_user.json()["accessToken"]
        change_profile_data = requests.patch(Api.patch_change_data,
                                             headers={"authorization": f"{auth_token}"}, data=patch_name)
        assert change_profile_data.json()["success"] == True and change_profile_data.status_code == 200
        del_user = requests.delete(Api.del_data, headers={"authorization": f"{auth_token}"})
        assert del_user.json() == ExpectedResults.delete_202 and del_user.status_code == 202

    @allure.title('Создаем -> логинимся -> редактируем email -> удаляем пользователя')
    @allure.description('ОР: статусы 200 и 202')
    def test_change_profile_email(self):
        patch_email = {"email": mail_generator()}
        new_user = requests.post(Api.post_reg, data=payload_new_user())
        auth_token = new_user.json()["accessToken"]
        change_profile_data = requests.patch(Api.patch_change_data,
                                             headers={"authorization": f"{auth_token}"}, data=patch_email)
        assert change_profile_data.json()["success"] == True and change_profile_data.status_code == 200
        del_user = requests.delete(Api.del_data, headers={"authorization": f"{auth_token}"})
        assert del_user.json() == ExpectedResults.delete_202 and del_user.status_code == 202

    @allure.title('Создаем -> логинимся -> редактируем password -> удаляем пользователя')
    @allure.description('ОР: статусы 200 и 202')
    def test_change_profile_password(self):
        patch_password = {"email": password_generator()}
        new_user = requests.post(Api.post_reg, data=payload_new_user())
        auth_token = new_user.json()["accessToken"]
        change_profile_data = requests.patch(Api.patch_change_data,
                                             headers={"authorization": f"{auth_token}"}, data=patch_password)
        assert change_profile_data.json()["success"] == True and change_profile_data.status_code == 200
        del_user = requests.delete(Api.del_data, headers={"authorization": f"{auth_token}"})
        assert del_user.json() == ExpectedResults.delete_202 and del_user.status_code == 202