import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSlowCalculator:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        yield
        self.driver.quit()

    def input_delay(self, delay):

        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()  # Очищаем поле ввода перед вводом нового значения
        delay_input.send_keys(delay)

    def click_button(self, value):

        button = self.driver.find_element(By.CSS_SELECTOR, f"button[value='{value}']")
        button.click()

    def test_calculator_result(self, setup):

        delay_value = "45"
        self.input_delay(delay_value)

        # Нажимаем кнопки
        self.click_button('7')
        self.click_button('+')
        self.click_button('8')
        self.click_button('=')

        # Ожидание
        result_element = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#result"))
        )

        # Проверяем, что результат равен 15
        assert result_element.text == "15", f"Expected result to be '15', but got '{result_element.text}'"
