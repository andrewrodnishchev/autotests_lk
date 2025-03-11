import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()

    # Добавляем задержку перед открытием страницы
    time.sleep(2)  # Задержка в 2 секунды

    # Переход на страницу входа
    driver.get('http://lk.corp.dev.ru/Account/Login?returnUrl=%2FClientOrg')

    # Ожидание загрузки страницы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[1]/input'))
    )

    yield driver  # Возвращает драйвер для использования в тестах
    driver.quit()  # Закрывает драйвер после завершения тестов
