import pytest	
from selenium import webdriver # импорт драйвера
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_browser():
    # Инициализация драйвера
    driver = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
    driver.maximize_window()  # Развернуть окно во весь экран
    yield driver
    # Завершение работы драйвера
    driver.quit()