from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

def after_all(context):
    context.driver.quit()
