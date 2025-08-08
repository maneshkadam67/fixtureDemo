import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_select_option:

    def test_select_option(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)
        self.driver.find_element(By.NAME, "login-button").click()
        time.sleep(4)
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        elements=self.driver.find_elements(By.XPATH,"//div[@class='inventory_list']/div")
        for i in range(len(elements)):
            if "Sauce Labs Bike Light" in elements[i].text:
                self.driver.find_element(By.XPATH,f"(// div[@class ='inventory_list'] // button[@ class ='btn btn_primary btn_small btn_inventory '])[{i}]").click()
                break
        time.sleep(4)





