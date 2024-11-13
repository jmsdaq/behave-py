from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory import InventoryPage
from cart_page import CartPage
import time

@given('I open the login page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get('https://www.saucedemo.com')
    context.login_page = LoginPage(context.driver)

@when('I enter "{username}" and "{password}" as credentials')
def step_impl(context, username, password):
    context.login_page.enter_credentials(username, password)
    context.login_page.click_login()

@then('I should be redirected to the inventory page')
def step_impl(context):
    context.inventory_page = InventoryPage(context.driver)
    time.sleep(2)
    assert context.inventory_page.is_redirected_to_inventory()
    context.driver.quit()

# New steps for adding item to cart
@given('I am logged in')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get('https://www.saucedemo.com')
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_credentials('standard_user', 'secret_sauce')
    context.login_page.click_login()
    context.inventory_page = InventoryPage(context.driver)

@when('I add an item to the cart')
def step_impl(context):
    context.inventory_page.add_item_to_cart()

@then('the item should appear in the cart')
def step_impl(context):
    context.inventory_page.go_to_cart()  # Go to cart page
    cart_page = CartPage(context.driver)  # Initialize CartPage
    assert cart_page.is_item_in_cart()  # Verify item in cart
    context.driver.quit()
