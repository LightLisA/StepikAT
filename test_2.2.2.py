from selenium import webdriver
import time
import math

link = "https://suninjuly.github.io/execute_script.html"
brouser = webdriver.Chrome()
brouser.get(link)

# копируем число из строки
num_a = brouser.find_element_by_css_selector("#input_value")
get_a = num_a.text

# Посчитать математическую функцию
def x_a(get_a):
	return str(math.log(abs(12*math.sin(int(get_a)))))
	
# Ввести ответ в текстовое поле
text_a = brouser.find_element_by_css_selector("#answer")
text_a.send_keys(x_a(get_a))

# Отметить checkbox "Подтверждаю, что являюсь роботом"
checkbox = brouser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()

# проскролюем страницу до Люди рулят (JavaScript)
brouser.execute_script("window.scrollBy(0,200);")

# Отметить radiobutton "Подтверждаю, что являюсь роботом"
RadioButton = brouser.find_element_by_css_selector("#robotsRule")
RadioButton.click()

# нажать кнопку Отправить
button = brouser.find_element_by_css_selector("button.btn")
button.click()

# ждем 5 cek чтобы взглянуть
time.sleep(5)

# закрываем
brouser.quit()
