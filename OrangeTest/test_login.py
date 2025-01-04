import pytest
from selenium.webdriver.common.by import By
import requests

def test_add_admin_user(driver, login):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    driver.find_element(By.ID, "btnAdd").click()
    driver.find_element(By.ID, "systemUser_userType").select_by_visible_text("Admin")
    driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys("Test User1")
    driver.find_element(By.ID, "systemUser_userName").send_keys("testUser1")
    driver.find_element(By.ID, "systemUser_status").select_by_visible_text("Enabled")
    driver.find_element(By.ID, "btnSave").click()
    # Add assertions to validate user addition

def test_add_ess_user(driver, login):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    driver.find_element(By.ID, "btnAdd").click()
    driver.find_element(By.ID, "systemUser_userType").select_by_visible_text("ESS")
    driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys("Test User2")
    driver.find_element(By.ID, "systemUser_userName").send_keys("testUser2")
    driver.find_element(By.ID, "systemUser_status").select_by_visible_text("Disabled")
    driver.find_element(By.ID, "btnSave").click()
    # Add assertions to validate user addition

def test_search_user(driver, login):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    driver.find_element(By.ID, "searchSystemUser_userName").send_keys("testUser1")
    driver.find_element(By.ID, "searchBtn").click()
    # Add assertions to validate search results

def test_reset_search(driver, login):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    driver.find_element(By.ID, "searchSystemUser_userName").send_keys("testUser1")
    driver.find_element(By.ID, "resetBtn").click()
    # Add assertions to validate reset functionality

def test_delete_user(driver, login):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    driver.find_element(By.ID, "searchSystemUser_userName").send_keys("testUser2")
    driver.find_element(By.ID, "searchBtn").click()
    driver.find_element(By.NAME, "chkSelectRow[]").click()
    driver.find_element(By.ID, "btnDelete").click()
    driver.find_element(By.ID, "dialogDeleteBtn").click()
    # Add assertions to validate user deletion

def test_validate_user_deletion_in_backend():
    # Sample SQL validation (assuming a function `execute_sql_query` is defined)
    result = execute_sql_query("SELECT * FROM users WHERE username='testUser2'")
    assert len(result) == 0

def test_validate_user_records_with_api():
    response = requests.get("https://api.example.com/users")
    assert response.status_code == 200
    users = response.json()
    # Add assertions to validate the user records