import sqlite3
import time

import pytest
import requests

from tests.models.users import User
from tests.page_objects.admin_page import AdminPage
from utils.global_values import USERS_URL, BASE_URL


class TestAdminPage:

    def test_this(self, global_values):
        print("\r\r")
        print("Employee Name, ", global_values["test_user_1"].employee_name)
        print("password, ", global_values["test_user_1"].password)
        print("username, ", global_values["test_user_1"].username)
        print("role, ", global_values["test_user_1"].role)
        print("status, ", global_values["test_user_1"].status)

    def test_add_admin_user(self, driver, login, global_values):
        admin_page = AdminPage(driver)
        driver.get(USERS_URL)
        admin_page.click_add_button()
        admin_page.select_user_type_admin()
        admin_page.select_status_enabled()
        admin_page.enter_employee_name(admin_page.get_employee_name())
        admin_page.enter_username(global_values["test_user_1"].username)
        admin_page.enter_password(global_values["test_user_1"].password)
        admin_page.enter_confirm_password(global_values["test_user_1"].password)
        admin_page.click_save_button()
        search_results = admin_page.search_user(global_values["test_user_1"].username)
        print(search_results)
        # Add assertions to validate user addition

    def test_add_ess_user(self, driver, login, global_values):
        admin_page = AdminPage(driver)
        driver.get(USERS_URL)
        admin_page.click_add_button()
        admin_page.select_user_type_ess()
        admin_page.enter_employee_name(admin_page.get_employee_name())
        admin_page.enter_username(global_values["test_user_2"].username)
        admin_page.enter_password(global_values["test_user_2"].password)
        admin_page.enter_confirm_password(global_values["test_user_2"].password)
        admin_page.select_status_disabled()
        admin_page.click_save_button()
        search_results = admin_page.search_user(global_values["test_user_2"].username)
        print(search_results)
        # Add assertions to validate user addition


    def test_search_and_reset(driver, login, global_values):
        admin_page = AdminPage(driver)
        driver.get(USERS_URL)
        admin_page.search_user(global_values["test_user_2"].username)
        records_found = admin_page.records_found_count()
        admin_page.click_reset_button()
        records_found_after_reset = admin_page.records_found_count()
        assert records_found != records_found_after_reset, "Records found should not be equal after reset"
    # Add assertions to validate search results



    def test_delete_user(driver, login, global_values):
        admin_page = AdminPage(driver)
        driver.get(USERS_URL)
        admin_page.delete_user(global_values["test_user_2"].username)
        search_results = admin_page.search_user(global_values["test_user_2"].username)
        assert search_results is None, "User should not be found"

        conn = sqlite3.connect('path/to/your/database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER WHERE username = ?", (global_values["test_user_2"].username,))
        user = cursor.fetchone()
        conn.close()
        assert user is None, "User should not be found in the database"
        # Add assertions to validate user deletion

    def test_API(driver, login, global_values):
        admin_page = AdminPage(driver)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        page_results = admin_page.search_user(global_values["test_user_1"].username)

        # API call
        response = requests.get(f"{BASE_URL}/users", params={"username": global_values["test_user_1"].username})
        response_json = response.json()

        # Assert that the JSON returned matches the page results
        assert response_json == page_results, "API response does not match the page results"


