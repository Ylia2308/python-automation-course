from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/classattr")

    # Нахождение кнопки по CSS-классу и клик по ней
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    blue_button.click()

    time.sleep(5)

finally:
    # Закрытие браузера
    driver.quit()
