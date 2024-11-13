from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_redirected_to_inventory(self):
        return "inventory" in self.driver.current_url
