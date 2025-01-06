import time

import pytest

from tests.models.users import User
from tests.page_objects.admin_page import AdminPage
from utils.global_values import USERS_URL


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

        print(global_values["test_user_1"].username)
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

    def test_add_ess_user(self, driver, login):
        admin_page = AdminPage(driver)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        admin_page.click_add_button()
        admin_page.select_user_type_ess()
        admin_page.enter_employee_name("Test User2")
        admin_page.enter_username("testUser2")
        admin_page.select_status_disabled()
        admin_page.click_save_button()
        # Add assertions to validate user addition

    def test_search_user(driver, login):
        admin_page = AdminPage(driver)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        admin_page.search_user("testUser1")
        # Add assertions to validate search results

    def test_reset_search(driver, login):
        admin_page = AdminPage(driver)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        admin_page.search_user("testUser1")
        admin_page.reset_search()
        # Add assertions to validate reset functionality

    def test_delete_user(driver, login):
        admin_page = AdminPage(driver)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        admin_page.search_user("testUser2")
        admin_page.delete_user()
        # Add assertions to validate user deletion

    def get(self, BASE_URL):
        pass
