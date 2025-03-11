import pytest

from autotests.pages.change_password_page import ProfilePage
from autotests.tests.test_login_page import LoginPage

class TestProfileManagement:
    @pytest.fixture
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.profile_page = ProfilePage(self.driver)

    def test_change_password(self, setup):
        # Авторизация
        self.login_page.login("test@safib.ru", "1")  # Замените на ваш старый пароль

        # Переход в профиль
        self.profile_page.navigate_to_profile()

        # Изменение пароля
        success_message = self.profile_page.change_password("1", "1")  # Замените на ваши пароли

        # Проверка успешного изменения пароля
        assert success_message == "Пароль успешно изменен.", "Сообщение об успешном изменении пароля не появилось."

