import time
import os
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("Name")

    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys("Lastname")

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("email@email.com")

    file_upload = browser.find_element_by_css_selector("[name='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'lesson2_step8_file.txt')  # добавляем к этому пути имя файла
    file_upload.send_keys(file_path)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
