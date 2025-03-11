import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_profile(self):
        wait = WebDriverWait(self.driver, 10)

        # Ожидаем и кликаем по кнопке "Профиль"
        profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/div/nav/ul/li/a/span")))  # Замените на актуальный XPath
        profile_button.click()

        # Ожидаем и кликаем по дополнительной кнопке профиля
        additional_profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/div/nav/ul/li/div/div[2]/a[1]")))  # Замените на актуальный XPath
        additional_profile_button.click()

    def change_password(self, old_password, new_password):
        wait = WebDriverWait(self.driver, 10)

        # Переход во вкладку безопасность
        security_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/ul/li[2]/a")))  # Замените на актуальный XPath
        security_tab.click()

        # Нажимаем на кнопку изменить пароль
        change_password_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/a")))  # Замените на актуальный XPath
        change_password_button.click()

        # Вводим старый пароль
        old_password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div[2]/form/div[1]/div/input")))  # Замените на актуальный XPath
        old_password_input.send_keys(old_password)

        # Вводим новый пароль
        new_password_input = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div[2]/form/div[2]/div/input")  # Замените на актуальный XPath
        new_password_input.send_keys(new_password)

        # Подтверждаем новый пароль
        confirm_password_input = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div[2]/form/div[3]/div/input")  # Замените на актуальный XPath
        confirm_password_input.send_keys(new_password)

        # Нажимаем на кнопку сохранить
        save_button = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div[2]/form/div[5]/button[1]")  # Замените на актуальный XPath
        save_button.click()

        time.sleep(1)


    # Ожидаем появления сообщения об успешном изменении пароля
        success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div")))  # Замените на актуальный XPath
        return success_message.text
