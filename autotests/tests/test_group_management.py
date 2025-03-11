import time

import pytest
from selenium.webdriver.common.by import By

from autotests.pages.group_management_page import MyAssistantPage
from autotests.tests.test_login_page import LoginPage

class TestGroupManagement:
    @pytest.fixture
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.my_assistant_page = MyAssistantPage(self.driver)

    def test_add_and_delete_group(self, setup):
    # Авторизация
        self.login_page.login("rodnischev@safib.ru", "1")  # Замените на ваш пароль

    # Переход к "Мой ассистент"
        self.my_assistant_page.click_my_assistant()
        self.my_assistant_page.click_my_assistant2()

    # Нажимаем на кнопку "Добавить группу"
        self.my_assistant_page.click_add_group()

    # Вводим название группы
        group_name = "ТестГруппа"
        self.my_assistant_page.enter_group_name(group_name)

    # Нажимаем на кнопку "Сохранить"
        self.my_assistant_page.click_save()

    # Ждем, чтобы сообщение успело появиться
        time.sleep(1)

    # Проверяем, что появилось уведомление о создании группы
        success_message = self.my_assistant_page.get_success_message()
        assert "Группа устройств успешно создана" in success_message, "Сообщение об успешном создании группы не появилось."

    # Ждем пару секунд
        self.driver.implicitly_wait(2)

    # Нажимаем на кнопку "Действия"
        self.my_assistant_page.click_actions()

    # Нажимаем на кнопку "Удалить"
        self.my_assistant_page.click_delete()

    # Подтверждаем удаление
        self.my_assistant_page.confirm_delete()

    # Ждем, чтобы изменения успели примениться
        self.driver.implicitly_wait(2)


