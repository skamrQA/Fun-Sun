import allure
import pytest
from page.main_page import MainPage
from conftest import chrome_browser



# TEST1
@allure.title("Проверка авторизации на сайте")
@allure.description("Тест проверяет авторизацию на сайте")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_sing_in(chrome_browser):
    tour_main = MainPage(chrome_browser)
    tour_main.sing_in()


# TEST2
@allure.title("Провека поля 'Откуда' на ввод кирилицей")
@allure.description("Тест проверяет поле 'Откуда' на ввод кирилицей")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_input_from(chrome_browser):
    tour_main = MainPage(chrome_browser)
    tour_main.input_from()


# TEST3
@allure.title("Провека поля страны 'Куда' на ввод кирилицей")
@allure.description("Тест проверяет поле страны 'Куда' на ввод кирилицей")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_input_where(chrome_browser):
    tour_main = MainPage(chrome_browser)
    tour_main.input_where()


# TEST4
@allure.title("Провека поля 'Дата вылета' на кликабельность")
@allure.description("Тест проверяет кликабельность поля 'Дата вылета'")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_flight_date(chrome_browser):
    tour_main = MainPage(chrome_browser)
    tour_main.flight_date()


# TEST5
@allure.title("Провека поля 'Длительность' и на кликабельность + нажатие кнопки 'Найти'")
@allure.description(
    "Тест проверяет поле 'Длительность' на кликабельность + нажатие кнопки 'Найти' 'Откуда' на ввод кирилицей")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_duration(chrome_browser):
    tour_main = MainPage(chrome_browser)
    tour_main.duration()


