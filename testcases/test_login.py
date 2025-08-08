import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_LoginTest:

    def test_login(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)
        self.driver.find_element(By.NAME, "login-button").click()
        time.sleep(4)
        assert "Swag Labs" in self.driver.title

    def test_select_other_option(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)
        self.driver.find_element(By.NAME, "login-button").click()
        time.sleep(4)
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        elements = self.driver.find_elements(By.XPATH, "//nav[@class='bm-item-list']/a")
        for element in elements:
            if element.text == "About":
                element.click()
                break
        print("clicked on about..................................")
        assert "Cross Browser Testing, Selenium Testing & Mobile Testing" in self.driver.title





