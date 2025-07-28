from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Находим синюю кнопку по ее классу 
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

    # Кликаем по кнопке
    blue_button.click()

    # Задержка для наблюдения результата 
    time.sleep(5)

finally:
    # Закрываем браузер
    driver.quit()
