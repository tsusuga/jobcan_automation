import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--headless')

print('connectiong to remote browser...')
driver = webdriver.Chrome(options=options)

driver.get('https://id.jobcan.jp/users/sign_in?app_key=atd')
print(driver.current_url)

time.sleep(1)

# ログイン情報入力欄の要素取得
id_input = driver.find_element_by_xpath("/html/body/div[@class='col-sm-6 sign-in-left-container']/div[@class='sign-in-panels-login']/div[@class='panel panel-default']/div[@class='panel-body']/form[@id='new_user']/div[@id='login_input']/label[@class='form__label'][1]/input[@id='user_email']")

pw_input = driver.find_element_by_xpath("/html/body/div[@class='col-sm-6 sign-in-left-container']/div[@class='sign-in-panels-login']/div[@class='panel panel-default']/div[@class='panel-body']/form[@id='new_user']/div[@id='login_input']/label[@class='form__label'][2]/input[@id='user_password']")

login_button = driver.find_element_by_xpath("/html/body/div[@class='col-sm-6 sign-in-left-container']/div[@class='sign-in-panels-login']/div[@class='panel panel-default']/div[@class='panel-body']/form[@id='new_user']/input[@id='login_button']")

# load_dotenv()
# account_id = os.getenv('ID')
# account_pw = os.getenv('PW')

id_input.send_keys("avs")
# pw_input.send_keys("ddd")

# login_button.send_keys(Keys.ENTER)