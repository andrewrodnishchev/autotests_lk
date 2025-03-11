import pytest
import allure
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Ожидаем, пока элементы будут доступны
        self.username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[1]/input'))
        )
        self.password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[2]/input'))
        )
        self.login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/form/button'))
        )

    def login(self, username, password):
        self.username_input.clear()  # Очистка поля перед вводом
        self.username_input.send_keys(username)
        self.password_input.clear()  # Очистка поля перед вводом
        self.password_input.send_keys(password)
        self.login_button.click()

    def get_error_message(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="toast-container"]/div/div'))
            ).text
        except TimeoutException:
            return "Сообщение об ошибке не найдено"


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


@allure.feature('User  Authentication')
@allure.story('Successful Login')
def test_successful_login(driver):
    login_page = LoginPage(driver)

    # Ввод корректных данных
    login_page.login('test@safib.ru', '1')

    # Проверка URL после входа
    WebDriverWait(driver, 10).until(EC.url_to_be('http://lk.corp.dev.ru/ClientOrg'))
    assert driver.current_url == 'http://lk.corp.dev.ru/ClientOrg'


@allure.feature('User  Authentication')
@allure.story('Unsuccessful Login')
def test_unsuccessful_login(driver):
    login_page = LoginPage(driver)

    # Ввод некорректных данных
    login_page.login('invalid_user', 'invalid_password')

    # Получение сообщения об ошибке
    error_message = login_page.get_error_message()

    # Проверка сообщения об ошибке
    assert error_message == 'Неверно указан логин или пароль'


if __name__ == "__main__":
    pytest.main()
