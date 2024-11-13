from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
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
