
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # Вызов веб-драйвера
actions = ActionChains(driver) # Двоной клик
wait = WebDriverWait(driver, 5) # Ожидание 5 сек

driver.get("https://fstravel.com")
driver.maximize_window() # Развернуть окно во весь экран
driver.find_element(By.CSS_SELECTOR, 'div.account__auth').click() # Нажатие на кнопку профиля для авторизации
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('skamrtest@gmail.com') # Заполнение поля "Email"
driver.find_element(By.CSS_SELECTOR, 'input#password.form__field').send_keys('是是是是是是') # Заполнение поля "Пароль"
driver.find_element(By.CSS_SELECTOR, 'input[value="Войти"]').click() # Нажатие кнопки "Войти"
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.v-departure__pinput__input.trslt'))) # Ждём 5 сек пока не станет кликабкльным
driver.find_element(By.CSS_SELECTOR, 'div.v-text-2.v-departure__title.trslt').click() # Нажатие кнопки "Откуда" 
actions.double_click(driver.find_element(By.CSS_SELECTOR, 'input.v-departure__pinput__input.trslt')) # Двойное нажатие кнопки "Откуда" по названию гоорода
driver.find_element(By.CSS_SELECTOR, 'input.v-departure__pinput__input.trslt').clear() # Очистка поля на случий наличия названия города
driver.find_element(By.CSS_SELECTOR, 'input.v-departure__pinput__input.trslt').send_keys('Санкт-Петербург') # Заполнение поля "Откуда"
actions.double_click(driver.find_element(By.CSS_SELECTOR, 'input[type="text"].arrival-country-field__pinput_input'))
driver.find_element(By.CSS_SELECTOR, 'div.v-text-2.arrival-country-field__pinput_title').clear()
driver.find_element(By.CSS_SELECTOR, 'input[type="text"].arrival-country-field__pinput_input').send_keys('ОАЭ')

driver.quit()

if __name__ == "__main__":
    pytest.main()