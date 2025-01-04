import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element_by_name("username").send_keys("Admin")
    driver.find_element_by_name("password").send_keys("admin123")
    driver.find_element_by_css_selector("button[type='submit']").click()