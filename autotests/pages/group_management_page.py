import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyAssistantPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_my_assistant(self):
        my_assistant_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/div/ul/li[1]/a/span[1]")))
        my_assistant_button.click()

    def click_my_assistant2(self):
        my_assistant_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/div/ul/li[1]/ul/li[1]/a")))
        my_assistant_button.click()

    def click_add_group(self):
        add_group_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/a[1]")))
        add_group_button.click()

    def enter_group_name(self, group_name):
        group_name_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input")))
        group_name_input.send_keys(group_name)

    def click_save(self):
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div/button")))
        save_button.click()

        time.sleep(1)

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div"))).text

    def click_actions(self):
        actions_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[5]/div/div/i")))
        actions_button.click()

    def click_delete(self):
        delete_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[5]/div/ul/li[2]/a")))
        delete_button.click()

    def confirm_delete(self):
        confirm_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[2]/button[1]")))
        confirm_button.click()
