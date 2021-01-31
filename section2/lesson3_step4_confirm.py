import time
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input_value = browser.find_element_by_id("input_value")
    input_value_text = input_value.text
    y = calc(input_value_text)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)

    button2 = browser.find_element_by_css_selector("[type='submit']")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
