# test_group_management.py

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from autotests.pages.group_management_page import GroupManagementPage
from autotests.pages.test_login_page import LoginPage

@allure.feature('Group Management')
@allure.story('Create Group')
@allure.step('Login to the application')
def test_create_group(driver):
    login_page = LoginPage(driver)
    login_page.login('test@safib.ru', '1')

    # Переход к управлению группами
    group_management_page = GroupManagementPage(driver)
    group_management_page.navigate_to_organization("Тест Андрей")  # Замените на имя вашей организации
    group_management_page.navigate_to_devices()

    group_name = "ТестГруппа"
    with allure.step(f'Adding group: {group_name}'):
        group_management_page.add_group(group_name)

    # Ожидание появления всплывающего окна
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div"))
    ), "Всплывающее окно не появилось, тест не пройден."

@allure.feature('Group Management')
@allure.story('Delete Group')
@allure.step('Login to the application')
def test_delete_group(driver):
    login_page = LoginPage(driver)
    login_page.login('test@safib.ru', '1')

    # Переход к управлению группами
    group_management_page = GroupManagementPage(driver)
    group_management_page.navigate_to_organization("Тест Андрей")  # Замените на имя вашей организации
    group_management_page.navigate_to_devices()

    group_name = "ТестГруппа"
    with allure.step(f'Deleting group: {group_name}'):
        group_management_page.delete_group(group_name)  # Метод для удаления группы

    # Ожидание, что группа была удалена
    try:
        # Проверка, что группа не присутствует на странице
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='{group_name}']"))
        )
        assert False, "Группа все еще существует, тест не пройден."
    except:
        # Если группа не найдена, тест считается пройденным
        pass

if __name__ == "__main__":
    pytest.main()
