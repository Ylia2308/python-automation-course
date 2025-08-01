from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Путь к ChromeDriver
driver_path = "C:\Users\aiale\Desktop\Все по учебе\chromedriver-win64\chromedriver.exe" 
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # На страницу
    driver.get('http://uitestingplayground.com/ajax')
    
    # Синяя кнопкуа
    button = driver.find_element(By.ID, 'ajaxButton')
    button.click()
    
    # Текст из зеленой плашки
    result = driver.find_element(By.ID, 'ajaxContent').text
    
    # Текст в консоль
    print(result)

finally:
    # Закройте драйвер
    driver.quit()
