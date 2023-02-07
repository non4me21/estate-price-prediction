from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest

def test_price_show_up():
    driver = webdriver.Safari()
    driver.get('http://localhost:3000')
    address = driver.find_element(By.NAME, 'address')
    address.send_keys('Wroclaw, rynek')
    area = driver.find_element(By.NAME, 'area')
    area.send_keys('60')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    rooms = Select(driver.find_element(By.NAME, 'rooms'))
    rooms.select_by_visible_text('3')
    button = driver.find_element(By.NAME, 'submit')
    start = time.time()
    button.submit()
    sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    price = driver.find_element(By.CLASS_NAME, 'priceInfo')
    end = time.time()
    runtime = end - start
    print(runtime)
    assert 'Szacowana cena' in price.text
    assert 3 > runtime


def test_empty_textfield_info():
    driver = webdriver.Safari()
    driver.get('http://localhost:3000')
    area = driver.find_element(By.NAME, 'area')
    area.send_keys('60')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    rooms = Select(driver.find_element(By.NAME, 'rooms'))
    rooms.select_by_visible_text('3')
    button = driver.find_element(By.NAME, 'submit')
    button.submit()
    sleep(0.5)
    warning = driver.find_element(By.NAME, 'emptyText')
    assert 'Uzupełnij wszystkie pola' == warning.text


