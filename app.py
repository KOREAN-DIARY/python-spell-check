import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

from flask import Flask

app = Flask(__name__)


@app.route("/spell", methods=['GET'])
def check_spell():
    driver = webdriver.Chrome()
    url = "http://speller.cs.pusan.ac.kr/"
    driver.get(url)
    text_box = driver.find_element(By.XPATH, '//*[@id="text1"]')
    text_box.send_keys('심여를 기우려 만든 마춤뻡 검사기')
    text_button = driver.find_element(By.XPATH, '//*[@id="btnCheck"]')
    text_button.click()
    time.sleep(1)
    text_result = driver.find_element(By.XPATH, '/html/head/script[3]')
    text = text_result.get_attribute(('text'))
    json_object = json.loads(text.split('data = ')[1].split(';')[0])
    return json_object
