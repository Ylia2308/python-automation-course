import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Edge() 
    yield driver
    driver.quit()

class TestFormSubmission:
    def test_form_submission(self, driver: WebDriver):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполняем форму
        self.wait_for_element(driver, By.NAME, "first-name").send_keys("Иван")
        self.wait_for_element(driver, By.NAME, "last-name").send_keys("Петров")
        self.wait_for_element(driver, By.NAME, "address").send_keys("Ленина, 55-3")
        self.wait_for_element(driver, By.NAME, "e-mail").send_keys("test@skypro.com")
        self.wait_for_element(driver, By.NAME, "phone").send_keys("+7985899998787")
        self.wait_for_element(driver, By.NAME, "zip-code").send_keys("")  # Поле zip-code остается пустым
        self.wait_for_element(driver, By.NAME, "city").send_keys("Москва")
        self.wait_for_element(driver, By.NAME, "country").send_keys("Россия")
        self.wait_for_element(driver, By.NAME, "job-position").send_keys("QA")
        self.wait_for_element(driver, By.NAME, "company").send_keys("SkyPro")

        # Отправляем форму
        self.wait_for_element(driver, By.XPATH, "//button[@type='submit']").click()

        # Проверяем, что все поля, кроме zip-code, подсвечены зеленым
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
        ]

        for field_name in fields_to_check:
            field = self.wait_for_element(driver, By.NAME, field_name)
            assert "green" in field.get_attribute("class"), f"{field_name} поля подсвечены зеленым"

    @staticmethod
    def wait_for_element(driver, by, value):
        return WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((by, value))
        )

