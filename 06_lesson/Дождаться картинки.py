from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "C:\Users\aiale\Desktop\Все по учебе\chromedriver-win64\chromedriver.exe" 
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # На сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Все изображений
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    # Значение атрибута src у 3-й картинки
    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")  # Индексация с 0
        print(third_image_src)  # Вывод значения в консоль
    else:
        print("На странице меньше трех изображений.")

finally:
    # Закрыть браузер
    driver.quit()
