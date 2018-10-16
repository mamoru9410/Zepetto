from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import mysql.connector

class Action:

    # chromedriver.exeを使う
    driver = webdriver.Chrome("C:/Users/mk-da/Desktop/IAMT/chromedriver/chromedriver.exe")

    #chrome起動してInsutagramに移動
    driver.get("https://www.instagram.com/accounts/login")

    #DB接続
    conn = mysql.connector.connect(user='root', password='d3876476', host='localhost', database='laravel57')
    cur = conn.cursor()

    #ID,PASS取得
    cur.execute("select * FROM laravel57.account WHERE no = '1'")
    for row in cur.fetchall():
        user_id = row[1]
        password = row[2]

    #DB切断
    conn.close()
    cur.close()

    #ユーザID入力ボックスを探す
    useridBox = driver.find_element_by_name("username")
    #ユーザID入力
    useridBox.send_keys(user_id)

    #パスワード入力ボックスを探す
    passwordBox = driver.find_element_by_name("password")
    #パスワード入力
    passwordBox.send_keys(password)

     #ログインボタンを探す
    loginButton = driver.find_elements_by_tag_name("button")[1]
    #検索ボタンをクリック
    loginButton.click()

    driver.implicitly_wait(30)
    atodeButton = driver.find_element_by_css_selector("_3m3RQ _7XMpj")[0]
    atodeButton.click()