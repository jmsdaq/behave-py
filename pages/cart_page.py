from selenium.webdriver.common.by import By

class CartPage:
    ITEM_IN_CART = (By.XPATH, '//div[@class="cart_item"]')
    CHECKOUT_BUTTON = (By.XPATH, '//button[@id="checkout"]')

    def __init__(self, driver):
        self.driver = driver

    def is_item_in_cart(self):
        items = self.driver.find_elements(*self.ITEM_IN_CART)
        return len(items) > 0

    def proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
