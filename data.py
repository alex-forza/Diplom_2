class Urls:
    url = 'https://stellarburgers.nomoreparties.site'

class StaticData:
    static_user_email = "tat@ya.ru"
    static_user_password = "tat12345"
    static_user_payload = {
    "email": "tat@ya.ru",
    "password": "tat12345"
}

class ExpectedResults:
    error_403_exists = {"success": False, "message": "User already exists"}
    error_403_no_required_fields = {"success": False, "message": "Email, password and name are required fields"}
    error_403_unauthorized = {"success": False, "message": "email or password are incorrect"}
    error_401_unauthorized_user = {"success": False, "message": "You should be authorised"}
    error_403_token_bad_change_data = {"success": False, "message": "jwt malformed"}
    delete_202 = {"success": True, "message": "User successfully removed"}
    no_ingredient_error_400 = {"success": False, "message": "Ingredient ids must be provided"}

class Api:
    post_reg = f'{Urls.url}/api/auth/register'
    post_login = f'{Urls.url}/api/auth/login'
    patch_change_data = f'{Urls.url}/api/auth/user'
    get_data = f'{Urls.url}/api/auth/user'
    del_data = f'{Urls.url}/api/auth/user'
    post_create_order = f'{Urls.url}/api/orders'
    get_order = f'{Urls.url}/api/orders'
    get_all_orders = f'{Urls.url}/api/orders/all'
    get_ingredients = f'{Urls.url}/api/ingredients'