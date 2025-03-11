# group_management_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GroupManagementPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_organization(self, org_name):
        # Метод для навигации к определенной организации
        org_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[4]/a/h2"))
        )
        org_link.click()

    def navigate_to_devices(self):
        # Метод для перехода к разделу устройств
        devices_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/ul/li[2]/a"))
        )
        devices_link.click()

    def add_group(self, group_name):
        # Метод для добавления новой группы
        add_group_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/a[1]"))
        )
        add_group_button.click()

        group_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input"))
        )
        group_name_input.send_keys(group_name)

        save_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div/button")
        save_button.click()

    def delete_group(self, group_name):
        # Метод для удаления группы по имени
        group_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/div/div/i"))
        )
        group_element.click()

        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/div/ul/li[2]/a"))
        )
        delete_button.click()

        # Подтверждение удаления
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[2]/button[1]"))
        )
        confirm_button.click()
