import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from constants import MAIN_URL
from constants import MAIL
from constants import PASSWORD


class MainPage:
    def __init__(self, browser):
        self._browser = browser
        self._browser.get(MAIN_URL)
        self.actions = ActionChains(browser)  # Двоной клик
        self.wait = WebDriverWait(browser, 12)  # Ожидание 10 сек

    # TEST_1
    with allure.step("Проверка авторизации на сайте"):
        def sing_in(self):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//./div[@class="popmechanic-close"]')))  # Ждём 10 сек окна уведомления пока не станет кликабкльным
            self._browser.find_element(By.CSS_SELECTOR, '.popmechanic-close').click()  # Нажатие "Х" для закрытия
            self._browser.implicitly_wait(2)  # Вынужденое ожидание
            self._browser.find_element(By.CSS_SELECTOR,
                                       'div.account__auth').click()  # Нажатие на кнопку профиля для авторизации
            self._browser.find_element(By.XPATH, '//input[@name="email"]').send_keys(MAIL)  # Заполнение поля "Email"
            self._browser.find_element(By.CSS_SELECTOR, 'input#password.form__field').send_keys(
                PASSWORD)  # Заполнение поля "Пароль"
            self._browser.find_element(By.CSS_SELECTOR, 'input[value="Войти"]').click()  # Нажатие кнопки "Войти"

    # TEST_2
    with allure.step("Провека поля 'Откуда' на ввод кирилицей"):
        def input_from(self):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//./div[@class="popmechanic-close"]')))  # Ждём 10 сек окна уведомления пока не станет кликабкльным
            self._browser.find_element(By.XPATH, '//./div[@class="popmechanic-close"]').click()  # Нажатие "Х" для закрытия
            self._browser.implicitly_wait(2)  # Вынужденое ожидание
            self._browser.find_element(By.CSS_SELECTOR, 'div.v-text-2.v-departure__title.trslt').click()  # Нажатие кнопки "Откуда"
            self._browser.implicitly_wait(2)  # Вынужденое ожидание
            self._browser.find_element(By.CSS_SELECTOR, 'input.v-departure__pinput__input.trslt').clear()  # Очистка поля на случий наличия названия города
            self._browser.find_element(By.CSS_SELECTOR, 'input.v-departure__pinput__input.trslt').send_keys(
                'Санкт-Петербург')  # Ввод в поле "Откуда" на кририллице

    # TEST_3
    with allure.step("Провека поля страны 'Куда' на ввод кирилицей"):
        def input_where(self):
            self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 '//./div[@class="popmechanic-close"]')))  # Ждём 10 сек окна уведомления пока не станет кликабкльным
            self._browser.find_element(By.XPATH,
                                       '//./div[@class="popmechanic-close"]').click()  # Нажатие "Х" для закрытия
            self._browser.implicitly_wait(2)  # Вынужденое ожидание
            self._browser.find_element(By.XPATH,
                                       '(//./div/input[@placeholder="Страна, город, отель"])[1]').click()  # Нажатие кнопки "Куда" поле страны
            self._browser.find_element(By.XPATH,
                                       '(//./div/input[@placeholder="Страна, город, отель"])[1]').clear()  # Очистка поля на случий наличия названия города
            self._browser.find_element(By.XPATH, '(//./div/input[@placeholder="Страна, город, отель"])[1]').send_keys(
                'ОАЭ')  # Ввод в поле страны "Куда" на кририллице

    # TEST_4
    with allure.step("Провека поля 'Дата вылета' на кликабельность"):
        def flight_date(self):
            self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 '//./div[@class="popmechanic-close"]')))  # Ждём 10 сек окна уведомления пока не станет кликабкльным
            self._browser.find_element(By.XPATH,
                                       '//./div[@class="popmechanic-close"]').click()  # Нажатие "Х" для закрытия
            self._browser.implicitly_wait(2)  # Вынужденое ожидание
            self._browser.find_element(By.XPATH,
                                       '(//./div[@class="calendar__field-dates"])[1]').click()  # Нажатие кнопки "Дата вылета" поле с датой, поле развернулось
            self._browser.find_element(By.XPATH,
                                       '(//./div[@class="calendar__field-dates"])[1]').click()  # Нажатие кнопки "Дата вылета" поле с датой второй раз для скрытия

    # TEST_5
    with allure.step("Провека поля 'Длительность' на кликабельность + нажатие кнопки 'Найти'"):
        def duration(self):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//./div[@class="popmechanic-close"]')))  # Ждём 10 сек окна уведомления пока не станет кликабкльным
            self._browser.find_element(By.XPATH, '//./div[@class="popmechanic-close"]').click()  # Нажатие "Х" для закрытия
            self._browser.implicitly_wait(5)  # Вынужденое ожидание
            self._browser.find_element(By.CSS_SELECTOR, '.v-nights__pinput').click()  # Нажатие кнопки "Длительность" поле с кол-м, поле развернулось
            self._browser.implicitly_wait(2)  # Вынужденое ожидание
            self._browser.find_element(By.CSS_SELECTOR, '.v-nights__pinput').click()  # Нажатие кнопки "Длительность" поле с кол-м второй раз для скрытия
            self._browser.find_element(By.CSS_SELECTOR, 'button.v-btn-yellow.v-search-button[data-v-17b0dddb]').click()  # Нажатие кнопки "Найти"