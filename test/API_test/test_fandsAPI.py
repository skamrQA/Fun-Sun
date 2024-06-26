import allure
import pytest
import requests

base_url = "https://fstravel.com/api"

headers = { 

        'content-type': 'application/json',
        'x-csrf-token': "Py3VpOl1opcmtodQqRpinisQSa5gvQJNTCmZPYr8",
        'x-xsrf-token': "eyJpdiI6Img4Zm91RTdmOE4yWi94Ui9sVTFFUEE9PSIsInZhbHVlIjoiZU5MQVBVZllpNnhCdENUaUhaQkJQRmQrdVFhanB0SmkvaGFBNERkUW0xWUs1a3VlTDVDeWt6NkxpS1RYWjFOMUpYWVgraVpYcHVXbFdvZzVaNWhSMzZvV0NGMFhqVzgxVGlxRS9HN0lsK1VseCtUaGJlRVdIOHJkVnlqd1h1dHUiLCJtYWMiOiJkYTBkNmMzNWNlYTIxNDYzNWYxNTZiMTM5NTAyMjhhODA5NDY0MDcwOGYxOGMzMDYwZGZjZWIyMzIxNTRhY2JlIn0="

         
    }

# API_TEST_1
@allure.title("Регистрация полльзователя")
@allure.description("Тест проверяет регистрацию пользователя")
@allure.feature("REGISTRATION")
@allure.severity("critical")
@pytest.mark.positive_test
def test_registration_user():

    with allure.step("API. Отправка запроса на регистрацию пользователя"):
        user_data = {

        "email": "vkhub11692519@yandex.ru",
        "password": "是是是是是是",
        "phoneNumber": "+79874566888"
        
        }
        resp = requests.post(base_url+'/v1/account/sign-up-buyer', json=user_data, headers=headers)
    
    with allure.step("Проверка статуса ответа"):
        assert resp.status_code == 201, "Статус код не соответствует ожидаемому"

# API_TEST_2
@allure.title("Авторизация полльзователя")
@allure.description("Тест проверяет проверяет авториизацию пользователя")
@allure.feature("AUTHORIZATION")
@allure.severity("blocked")
@pytest.mark.positive_test
def test_authorization_user():
    
    with allure.step("api. Авторизация полльзователя через API"):
        user_data = {

        "email": "vkhub11692519@yandex.ru",
        "password": "是是是是是是"

        }
        resp = requests.post(base_url+'/login/signin', json=user_data, headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

# API_TEST_3
@allure.title("Поиск тура с заданными параметрами")
@allure.description("Тест проверяет поиск туров")
@allure.feature("SEARCH")
@allure.severity("critical")
@pytest.mark.positive_test
def test_search_tour(null=None):
    
    with allure.step("api. Поиск тура через API"):
        search_data = {
        
            "adults": 2,
            "arrivalCityIds": [],
            "arrivalCountry": 20625,
            "arrivalRegionIds": [],
            "children": [],
            "departureCityId": 526606,
            "departureCityName": null,
            "hotelIds": [],
            "maxNightsCount": 6,
            "minNightsCount": 6,
            "maxStartDate": "2024-07-07",
            "minStartDate": "2024-07-01",
            "fullsearch": true
        }
        resp = requests.post(base_url+'/Tours/GetPriceDynamics', json=search_data, headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

# API_TEST_4
@allure.title("Поиск авиабилетов с заданными параметрами")
@allure.description("Тест проверяет поиск авиабилетов")
@allure.feature("SEARCH_AIR")
@allure.severity("critical")
@pytest.mark.positive_test
def test_search_air():
    
    with allure.step("api. Поиск авиабилетов через API"):
        search_data = {
        
            "fromto1": "MOW-AER",
            "fromto2": "",
            "date1": "2024-06-30",
            "date2": "",
            "adults": 1,
            "children": 0,
            "infants": 0,
            "serviceclass": "economy"

        }
        resp = requests.post(base_url+'/avia/search', json=search_data, headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

# API TEST 5
@allure.title("Поиск отелей с заданными параметрами")
@allure.description("Тест проверяет поиск отелей")
@allure.feature("SEARCH_HOTEL")
@allure.severity("critical")
@pytest.mark.positive_test
def test_search_hotel():
    
    with allure.step("api. Поиск отелей через API"):
        search_data = {
        
            "adults": 2,
            "arrivalCityIds": [],
            "arrivalCountry": 18803,
            "arrivalRegionIds": [],
            "children": [],
            "departureCityId": 1,
            "departureCityName": null,
            "hotelIds": [],
            "maxNightsCount": 14,
            "minNightsCount": 14,
            "maxStartDate": "2024-07-13",
            "minStartDate": "2024-07-07",
            "fullsearch": true

        }
        resp = requests.post(base_url+'/avia/search', json=search_data, headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

