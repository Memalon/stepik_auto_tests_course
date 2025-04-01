from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ссылка
link = "https://suninjuly.github.io/math.html"

# запускаем браузер
browser = webdriver.Chrome()
# открываем ссылку
browser.get(link)

try:
    people_radio = browser.find_element(By.ID, "peopleRule")

    print(people_radio.get_attribute("name"))
    # Напечатает ruler, т.е. текстовое значение аттрибута name="ruler"

    print(people_radio.get_attribute("checked"))
    # Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.

    print(people_radio.get_attribute("href"))
    # Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"

finally:
    # закрыть тестовую сессию
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла