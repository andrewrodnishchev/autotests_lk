import pytest
from selenium.webdriver.common.by import By

from autotests.pages.organization_device_management_page import DevicePage
from autotests.tests.test_login_page import LoginPage

class TestDeviceManagement:
    @pytest.fixture
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.device_page = DevicePage(self.driver)

    def test_add_device(self, setup):
        # Авторизация
        self.login_page.login("test@safib.ru", "1")

        # Переход в организацию и устройства
        self.device_page.navigate_to_devices()

        # Добавление устройства
        self.device_page.add_device("135 026 892")

        # Проверка появления окна с идентификатором
        # Здесь мы можем оставить проверку на наличие окна, если это необходимо
        assert self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div").is_displayed(), "Окно добавления устройства не появилось."

    def test_delete_device(self, setup):
        # Авторизация
        self.login_page.login("test@safib.ru", "1")

        # Переход в организацию и устройства
        self.device_page.navigate_to_devices()

        # Удаление устройства
        self.device_page.delete_device("135 026 892")

        # Проверка удаления устройства
        assert "135 026 892" not in self.driver.page_source, "Идентификатор устройства все еще присутствует на странице."
