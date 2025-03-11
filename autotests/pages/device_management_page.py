from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DevicePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_devices(self):
        wait = WebDriverWait(self.driver, 10)

        # Ожидаем, пока элемент станет кликабельным, и кликаем по нему
        devices_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[4]/a/h2")))
        devices_link.click()

        # Ожидаем, пока второй элемент станет кликабельным, и кликаем по нему
        second_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/ul/li[2]/a")))
        second_link.click()

    def add_device(self, identifier):
        wait = WebDriverWait(self.driver, 10)

        # Ожидаем, пока элемент для добавления устройства станет кликабельным
        add_device_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/a[1]/i")))
        add_device_button.click()

        # Ожидаем, пока поле ввода идентификатора станет доступным
        identifier_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input")))
        identifier_input.send_keys(identifier)

        # Ожидаем, пока кнопка для подтверждения добавления устройства станет кликабельной
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div/button")
        submit_button.click()
        submit_button.click()

        # Ожидаем появления окна с заданным XPath
        wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div")))  # Ожидаем, пока элемент станет видимым

    def delete_device(self, identifier):
        wait = WebDriverWait(self.driver, 10)

        # Ожидаем, пока кнопка действий станет кликабельной и нажимаем на неё
        actions_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/div/div/i")))
        actions_button.click()

        # Ожидаем, пока кнопка "Удалить" станет кликабельной
        delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/div/ul/li[3]/a")))
        delete_button.click()

        # Ожидаем, пока кнопка подтверждения удаления станет кликабельной
        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[2]/button[1]")))
        confirm_button.click()

        # Ожидаем, пока элемент исчезнет
        wait.until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[2]/button[1]")))
