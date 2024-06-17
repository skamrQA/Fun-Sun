from selenium.webdriver.common.by import By
from constants import MAIN_URL

# class main_page:
#     def __init__(self, browser):
#         self.browser = browser
#         self.browser.get(MAIN_URL)
#         self.browser.maximize_window() # Развернуть окно во весь экран

#     #авторизация на сайте
#     def sing_in(self):
#         self.browser.find_element(By.CSS_SELECTOR, 'div.account__auth').click() # Нажатие на кнопку профиля для авторизации
#         self.browser.find_element(By.XPATH, '//input[@name="email"]').send_keys('skamrtest@gmail.com') # Заполнение поля "Email"
#         self.browser.find_element(By.CSS_SELECTOR, 'input#password.form__field').send_keys('是是是是是是') # Заполнение поля "Пароль"
#         self.browser.find_element(By.CSS_SELECTOR, 'input[value="Войти"]').click() # Нажатие кнопки "Войти"
        