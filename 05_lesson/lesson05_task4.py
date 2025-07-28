from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/login")
    
    # Поиск поля username и ввод значения
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    
    # Поиск поля password и ввод значения
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    
    # Поиск кнопки Login и нажатие на нее
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Ожидание для загрузки страницы 
    time.sleep(5)
    
    # Поиск элемента с зеленой плашкой и вывод текста в консоль
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print(success_message.text)

finally:
    # Закрытие браузера
    driver.quit()
