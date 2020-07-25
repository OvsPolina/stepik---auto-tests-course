from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element1=browser.find_element_by_css_selector("#num1")
    element2=browser.find_element_by_css_selector("#num2")
    x1=element1.text
    x2=element2.text
    y = int(x1)+int(x2)
    print(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

