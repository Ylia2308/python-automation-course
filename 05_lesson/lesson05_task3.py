from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Поиск текстового поля
    input_field = driver.find_element(By.TAG_NAME, "input")
    
    # Ввод текста "Sky"
    input_field.send_keys("Sky")
    
    # Ожидание для визуальной проверки
    time.sleep(5)
    
    # Очистка текстового поля
    input_field.clear()
    
    # Ввод текста "Pro"
    input_field.send_keys("Pro")
    
    # Ожидание для визуальной проверки
    time.sleep(5)

finally:
    # Закрытие браузера
    driver.quit()
