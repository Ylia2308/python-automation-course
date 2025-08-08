import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSlowCalculator:
    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Chrome()
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        yield driver 
        driver.quit()

    def input_delay(self, driver, delay):
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()  # Поле ввода
        delay_input.send_keys(delay)

    def click_button(self, driver, value):
        # Изменяем селектор для поиска кнопок
        button = driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def test_calculator_result(self, setup):
        driver = setup  
        delay_value = "45"
        self.input_delay(driver, delay_value)

        # Нажимаем кнопки
        self.click_button(driver, '7')  # Нажимаем кнопку '7'
        self.click_button(driver, '+')   # Нажимаем кнопку '+'
        self.click_button(driver, '8')   # Нажимаем кнопку '8'
        self.click_button(driver, '=')    # Нажимаем кнопку '='

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

        # Проверяем, что результат равен 15
        assert result_element.text == "15", f"Expected result to be '15', but got '{result_element.text}'"
