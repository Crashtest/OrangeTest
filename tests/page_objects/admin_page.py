# tests/page_objects/admin_page.py
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.employee_name = (By.CSS_SELECTOR, ".oxd-userdropdown-name")
        self.admin_section_crumb = (By.XPATH,
                                    "//*[contains(@class, 'oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module') and text()='Admin']")
        self.admin_button = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
        self.add_button = (By.XPATH,
                           "//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary') and text()=' Add ']")
        self.user_type_dropdown = (
        By.CSS_SELECTOR, ".oxd-select-text.oxd-select-text--active > .oxd-select-text-input:first-child")
        self.status_dropdown = (By.XPATH, "//div[contains(@class, 'oxd-select-text-input') and text()='-- Select --']")
        self.employee_name_input = (
        By.CSS_SELECTOR, ".oxd-autocomplete-text-input input[placeholder='Type for hints...']")
        self.username_input = (By.XPATH,
                               "//*[contains(@class, 'oxd-input-group oxd-input-field-bottom-space') and .//label[text()='Username']]//input")
        self.password_input = (By.XPATH,
                               "//div[contains(@class, 'oxd-input-group oxd-input-field-bottom-space') and .//label[text()='Password']]//input")
        self.password_confirm_input = (By.XPATH,
                                       "//div[contains(@class, 'oxd-input-group oxd-input-field-bottom-space') and .//label[text()='Confirm Password']]//input")
        self.save_button = (By.CSS_SELECTOR,
                            "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
        self.search_username_input = (
        By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input")
        self.search_button = (By.CSS_SELECTOR,
                              "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.oxd-table-filter > div.oxd-table-filter-area > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
        self.search_results = (
        By.CSS_SELECTOR, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div")
        self.reset_button = (By.ID, "resetBtn")
        self.delete_checkbox = (By.NAME, "chkSelectRow[]")
        self.delete_button = (By.ID, "btnDelete")
        self.confirm_delete_button = (
        By.CSS_SELECTOR, "oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin")
        self.add_user_dialog = (By.CSS_SELECTOR, "h6.orangehrm-main-title")
        self.user_records_table = (By.XPATH, "table.oxd-table.oxd-table")

    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.admin_section_crumb)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_add_user_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.add_user_dialog)
            )
            return True
        except TimeoutException:
            return False

    def get_employee_name(self):
        return self.driver.find_element(*self.employee_name).text

    def click_add_button(self):
        self.wait_for_page_to_load()
        self.driver.find_element(*self.add_button).click()

    def select_user_type(self, user_type):
        self.wait_for_add_user_to_load()
        dropdown_element = self.driver.find_element(*self.user_type_dropdown)
        dropdown_element.click()
        option = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{user_type}')]")
        option.click()

    def select_user_type_admin(self):
        self.wait_for_add_user_to_load()
        dropdown_element = self.driver.find_element(*self.user_type_dropdown)
        dropdown_element.click()
        option = self.driver.find_element(By.XPATH, f"//*[contains(text(), 'Admin')]")
        option.click()
        time.sleep(1)

    def select_user_type_ess(self):
        self.wait_for_add_user_to_load()
        dropdown_element = self.driver.find_element(*self.user_type_dropdown)
        dropdown_element.click()
        option = self.driver.find_element(By.XPATH, f"//*[contains(text(), 'ESS')]")
        option.click()
        time.sleep(1)

    def select_status_enabled(self):
        dropdown = self.driver.find_element(*self.status_dropdown)
        dropdown.click()
        option = self.driver.find_element(By.XPATH, f"//*[contains(text(), 'Enabled')]")
        option.click()

    def select_status_disabled(self):
        dropdown = self.driver.find_element(*self.status_dropdown)
        dropdown.click()
        option = self.driver.find_element(By.XPATH, f"//*[contains(text(), 'Disabled')]")
        option.click()

    def enter_employee_name(self, name):
        first_name = name.split(" ")[0]
        self.driver.find_element(*self.employee_name_input).send_keys(first_name)
        time.sleep(3)
        option = self.driver.find_element(By.XPATH, f"//div[contains(@class, '.orangehrm-card-container') and //*[starts-with(text(), '{first_name}')]")
        option.click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        time.sleep(1)
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(*self.password_confirm_input).send_keys(password)

    def click_save_button(self):
        self.driver.find_element(*self.save_button).click()

    def search_user(self, username):
        self.driver.find_element(*self.search_username_input).send_keys(username)
        self.driver.find_element(*self.search_button).click()
        results_table = self.driver.find_element(*self.user_records_table)
        return results_table

    def reset_search(self):
        self.driver.find_element(*self.reset_button).click()

    def delete_user(self):
        self.driver.find_element(*self.delete_checkbox).click()
        self.driver.find_element(*self.delete_button).click()
        self.driver.find_element(*self.confirm_delete_button).click()
