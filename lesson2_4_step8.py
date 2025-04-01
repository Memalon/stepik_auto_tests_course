# ЗАДАЧА
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond
import math
import time

link="http://suninjuly.github.io/explicit_wait2.html"

browser=webdriver.Chrome()
browser.get(link)

try:
    WebDriverWait(browser,12).until(exp_cond.text_to_be_present_in_element((By.ID,"price"),"$100"))
    browser.find_element(By.ID, "book").click()

    # нашли элемент с указагием значения х
    find_x= browser.find_element(By.ID,"input_value")
    print('Нашли элемент где прописан х')
    x = int(find_x.text)
    print('Извлелкли x=',x)

    # посчитали выражаение с х
    y = math.log(abs(12*math.sin(x)))
    print('Вычислили log(abs(12*math.sin(x))) =',y)

    # нашли текстовое поля для ввода результат
    inp = browser.find_element(By.ID,"answer")
    print('Нашли поле input для ввода текста')
    # ввели резульат
    inp.send_keys(str(y))
    print('Ввели текст в полне.')

    # нашли кнопку Submit и нажали отправить форму
    browser.find_element(By.ID,"solve").click()
    print('Нашли кнопку Submit и нажали отправить форму.')

finally:
    time.sleep(5)
    browser.quit()

# изменения для пробного коммита
print('Test: Done!')