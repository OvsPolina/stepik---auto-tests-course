from selenium import webdriver
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")
    button = browser.find_element_by_id("button")
    button.click()
finally:
    browser.quit()     

