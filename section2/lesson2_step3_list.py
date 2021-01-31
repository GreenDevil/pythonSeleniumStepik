import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num1_text = num1.text
    num2 = browser.find_element_by_id("num2")
    num2_text = num2.text

    sum = int(num1_text) + int(num2_text)

    print(sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum))

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
