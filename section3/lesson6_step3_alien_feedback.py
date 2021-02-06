import pytest
from selenium import webdriver
import time
import math


def get_answer():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    input_field = browser.find_element_by_tag_name("textarea")
    answer = get_answer()
    input_field.send_keys(str(answer))

    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    hint = browser.find_element_by_class_name("smart-hints__hint")
    assert hint.text == "Correct!", f"Expect text 'Correct!' but got {hint.text}"
