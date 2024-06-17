import pytest	
from selenium import webdriver # импорт драйвера
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_browser():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Завершение работы драйвера
    driver.quit()