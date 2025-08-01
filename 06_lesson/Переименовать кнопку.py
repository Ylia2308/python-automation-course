from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Путь к ChromeDriver
driver_path = "C:\Users\aiale\Desktop\Все по учебе\chromedriver-win64\chromedriver.exe" 
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # На сайт
    driver.get("http://uitestingplayground.com/textinput")

    # В поле ввода текст SkyPro
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear()  # Очистить поле ввода, если там что-то есть
    input_field.send_keys("SkyPro")

    # Синяя кнопка
    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    # Текст кнопки и выведите в консоль
    button_text = button.text
    print(button_text)  # Ожидается вывод "SkyPro"

finally:
    # Закрыть браузер
    driver.quit()