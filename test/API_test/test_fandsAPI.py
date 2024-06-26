import allure
import pytest
import requests

base_url = "https://fstravel.com/api"

headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'baggage':   'sentry-environment=production,sentry-release=RELEASETAG,sentry-public_key=22017e57f7a44c15a37b060e0b3b611d,sentry-trace_id=fbd755e412d34cfba5f2f1b35c3e56d1,sentry-sample_rate=1,sentry-sampled=true',
        'cache-control': 'no-cache',
        'cookie': '__ddg1_=HypnRAaYAWsGquKcD22J; advcake_track_id=dc080d18-e115-abe0-04d9-8ec6930aa407; advcake_session_id=3487c1ca-98ff-8a8c-342e-5a1d2d54bbab; tmr_lvid=be5909f262456802ec2a1f44445908cd; tmr_lvidTS=1704762700103; flocktory-uuid=9b7d49f7-98db-4684-aed3-57a0feed231a-0; _ym_uid=1704762699990773162; _ym_d=1718248758; _ymab_param=L01UDLX90FIU7Ysf3BAp1jDcLkhcP3wBdIPNEutqElD9crxjTTuQeNeZKgoi8O-SHhQHm7ZHCh5u8e5Av8F8OgiUJek; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ct=1700000000297128530; _ct_client_global_id=1199c556-6fcc-5dd4-a04d-3726c30abcd3; has_action=true; adrcid=AQxICIXpQ5gzwh-HeaMmx8A; r2UserId=1718680743049833; analytic_id=1718680743191777; cted=modId%3Dop885zi2%3Bclient_id%3D78345122.1718248756%3Bya_client_id%3D1704762699990773162; _sp_ses.03b1=*; _ym_isad=2; _ct_ids=op885zi2%3A42831%3A451536192; _ct_session_id=451536192; _ct_site_id=42831; _ym_visorc=b; domain_sid=zmv8MnKEOe0SRztyNAZo-%3A1719407261365; adrdel=1719407261676; _gid=GA1.2.391574372.1719407262; mindboxDeviceUUID=ecd52e72-81b5-41ce-8670-5a06bf0b6899; directCrm-session=%7B%22deviceGuid%22%3A%22ecd52e72-81b5-41ce-8670-5a06bf0b6899%22%7D; PHPSESSID=emh09hag6ec3c1admu7m0tl7bi; PageNumber=2; advcake_track_url=%3D20240624bgV1YMWzF1cM%2BgzTupK6L%2FKMJ0z%2BH%2B1oekSYzeV5f84Q1AFYL8HS58ZYVOa4p61291i%2Bf5AEss6COzSJBjXZkJhpELjD%2BJRZwRTsBjnirM%2BulGoKKgv6axS4R2hd46fW%2FUmYKeKCZMmQCavbcKqTp7f5q5U2eXkihvehllfFulPoguZEIExoiV798a2WkkvcgUAuBiHScXo1K336qWA41RnTN2UdHg4IzWrkdJmLBAR7vDVYqvRIzCcN%2FgxAC7IgeIqjOcrKTy1OdW58bcuRs9cZCHBluFEM0wVIkY%2FBeY8yfqwq7rgyL1z%2FirVgm4pPP4ow30hRCa9QHyH9bQMpXCAYqD89oVICR4J9UurOngzJXKBGqvtRFuFlbniwBkdzNfb%2FRSmEWsFHh4X%2BGB%2BcCai0zTGvQfRAtumIkACyYLXifZRX3Oh7Syq3Hps8k9FUnZmCz5hbtL9JHHdst2FDuAUs8lsuOwlEtgB8jWk21PsKVAY1jlOG8Zv%2FK58tEyLXPSkgB55lZICL%2FApR1KCfetiexS7Pr3df59wjQrXdMPOovnqxRDl6mBOmtsf7AvVXOBvyUhkJ1qVGRK1k%2Fcon0DKXy4tXbNNMubDBVUIkTfGXUoPYPcqoAjltbtDZalrFh00pV7DuBgYIIj4b2YwVOiE5ME92GVO6uYKBP34BldYY2%2By25cmN3Po%3D; _spx=eyJpZCI6ImRhOGM1MjI1LTcxNzgtNDQ1Yi1hYmM5LWNmODg5OGQ1MTY0MyIsInNvdXJjZSI6IiIsImZpeGVkIjp7InN0YWNrIjpbMCwxMjEzNzk0Mzc3XX19; _sp_id.03b1=2ab14360-a3f6-41d7-8604-401ba6db7002.1718248757.3.1719407313.1718683131.0b1d6605-eabd-48aa-845e-9d4c5d617d10; _ubtcuid=fe9bd14e-1f81-4f34-fa46-9f56773ffa3a; call_s=%3C\\u0021%3E%7B%22op885zi2%22%3A%5B1719409111%2C451536192%2C%7B%22346346%22%3A%22985422%22%7D%5D%2C%22d%22%3A2%7D%3C\\u0021%3E; _ga=GA1.2.78345122.1718248756; tmr_detect=0%7C1719407315641; _ga_GJ17DPCPJY=GS1.1.1719407260.3.1.1719407323.0.0.0; XSRF-TOKEN=eyJpdiI6IkN3akFReGluMEdTempFSXErTWhxS0E9PSIsInZhbHVlIjoiMlFrS0o4bE93dnl3VXBGN1QxWGY0ZDZBV3hwUzdJNnVZMUUzZGtKQzF4azVJdU1QOEdGbnQvbHNwRzJSS1Aycm5OS0ovU1lFUWpIQWpvQTdIWnBXV3J3K29HTnFoZFlFTWdlRzh0dVNuMTVaTXVTaXduNjRScWh5OTZBZzMrRTYiLCJtYWMiOiI5MWI1YjcwMjgxYWI5YzY4N2QxMGUzOTIxNzFhN2U5YWRmNDMxYWE4M2UzYTI3MjE4ODMwNDE4NjFlZDA1OGVmIn0%3D; funsan_session=eyJpdiI6IitWc2NXYU9rTHlYUTN1Y1g0QWZ0MWc9PSIsInZhbHVlIjoiZSs3ZnNjUDhBa1E0a2xJTnQwUTV4VytMVXBwcGRBaG04bDFzbVl0V2pUWjRibnViOVl3eUZyRTJEbHIyWkVIemYyd3ZJMjkwMTVsMFQ4UDF5ZEV0SjI4RXlOZTdzSGVUT1JSait5ZHAvMEhVNDJ5b1BIMlZ5M3FsNFdIT3B6Yk0iLCJtYWMiOiIwYzVlZDRmMjEwMTYxNTU2OWYzMGVlYmI5MjEzNGI5NmQ4ZjE4ZmNhYmFlZWFlYTQyNjJkNzM4YmUyOGUwODUyIn0%3D',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://fstravel.com/searchtour/country/asia/thailand?departureCityId=526606&arrivalCountryId=20625&minStartDate=2024-07-12&maxStartDate=2024-07-12&minNightsCount=6&maxNightsCount=6&adults=2&flightTypes=all&sort=recommendations_FS',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'fbd755e412d34cfba5f2f1b35c3e56d1-84e79863e7bd61af-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-csrf-token': 'je7JGunN5ZMMOfRYP3Dch2jDsPjKr8jI3nz0xYv3',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6IkN3akFReGluMEdTempFSXErTWhxS0E9PSIsInZhbHVlIjoiMlFrS0o4bE93dnl3VXBGN1QxWGY0ZDZBV3hwUzdJNnVZMUUzZGtKQzF4azVJdU1QOEdGbnQvbHNwRzJSS1Aycm5OS0ovU1lFUWpIQWpvQTdIWnBXV3J3K29HTnFoZFlFTWdlRzh0dVNuMTVaTXVTaXduNjRScWh5OTZBZzMrRTYiLCJtYWMiOiI5MWI1YjcwMjgxYWI5YzY4N2QxMGUzOTIxNzFhN2U5YWRmNDMxYWE4M2UzYTI3MjE4ODMwNDE4NjFlZDA1OGVmIn0='
    }


# API_TEST_1
@allure.title("Доступ к сайту")
@allure.description("Тест проверяет доступ к сайту")
@allure.feature("REGISTRATION")
@allure.severity("critical")
@pytest.mark.positive_test
def test_get_hotel():
    with allure.step("API. Проверка доступа к сайту"):

        resp = requests.get(base_url + '/geo/geo-object/267459/hotel', json=headers, headers=headers)

    with allure.step("Проверка статуса ответа"):
        assert resp.status_code == 200, "Статус код не соответствует ожидаемому"


# API_TEST_2
@allure.title("Авторизация полльзователя")
@allure.description("Тест проверяет проверяет авториизацию пользователя")
@allure.feature("AUTHORIZATION")
@allure.severity("blocked")
@pytest.mark.positive_test

def test_authorization_user():
    with allure.step("api. Авторизация полльзователя через API"):

        user_data = {

            "email": "skamrtest@gmail.com",
            "password": "是是是是是是"

        }
        resp = requests.post(base_url + '/login/signin', json=user_data, headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"


# API_TEST_3
@allure.title("Поиск тура с заданными параметрами")
@allure.description("Тест проверяет поиск туров")
@allure.feature("SEARCH")
@allure.severity("critical")
@pytest.mark.positive_test
def test_search_tour():
    with allure.step("api. Поиск тура через API"):

        search_data = {

            "adults": 2,
            "arrivalCityIds": [],
            "arrivalCountry": 20625,
            "arrivalRegionIds": [],
            "children": [],
            "departureCityId": 526606,
            "departureCityName": "",
            "hotelIds": [],
            "maxNightsCount": 6,
            "minNightsCount": 6,
            "maxStartDate": "2024-07-07",
            "minStartDate": "2024-07-01",
            "fullsearch": ""
        }
        resp = requests.post(base_url + '/Tours/GetPriceDynamics', json=search_data, headers=headers)
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
        resp = requests.post(base_url + '/avia/search', json=search_data, headers=headers)
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
            "departureCityName": "",
            "hotelIds": [],
            "maxNightsCount": 14,
            "minNightsCount": 7,
            "maxStartDate": "2024-07-13",
            "minStartDate": "2024-07-07",
            "fullsearch": ""

        }
        resp = requests.post(base_url + '/avia/search', json=search_data, headers=headers)
    assert resp.status_code == 201
    assert resp.headers["Content-Type"] == "application/json"

