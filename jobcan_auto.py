import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--headless')

print('connectiong to remote browser...')
driver = webdriver.Chrome(options=options)

url = 'https://id.jobcan.jp/users/sign_in?app_key=atd'
driver.get(url)
print(driver.current_url)

#ページ上のすべての要素が読み込まれるまで待機
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located)
#入力フォームを取得
id_input = driver.find_element_by_id('user_email')
pw_input = driver.find_element_by_id('user_password')
login_button = driver.find_element_by_id('login_button')
#.envファイルからログイン情報の取得
load_dotenv()
account_id = os.getenv('ID')
account_pw = os.getenv('PW')
#フォームにログイン情報を入力してログインボタンをPUSH
id_input.send_keys(account_id)
pw_input.send_keys(account_pw)
login_button.send_keys(Keys.ENTER)
#打刻ボタンを取得してPUSH
wait.until(EC.presence_of_all_elements_located)
audit_button = driver.find_element_by_id('adit-button-push')
audit_button.send_keys(Keys.ENTER)
#確認のため停止
time.sleep(1000)

driver.quit()
