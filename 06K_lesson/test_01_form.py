import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFormSubmission:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Edge()  
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        yield
        self.driver.quit()

    def test_form_submission(self, setup):
        # Заполнение формы
        self.driver.find_element(By.NAME, "firstname").send_keys("Иван")
        self.driver.find_element(By.NAME, "lastname").send_keys("Петров")
        self.driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self.driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        self.driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self.driver.find_element(By.NAME, "zipcode").send_keys("")  # Оставляем пустым
        self.driver.find_element(By.NAME, "city").send_keys("Москва")
        self.driver.find_element(By.NAME, "country").send_keys("Россия")
        self.driver.find_element(By.NAME, "job").send_keys("QA")
        self.driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Нажимаем кнопку Submit
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()

       # Ожидание, пока поля будут видимыми и проверяем их цвет
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "firstname"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "lastname"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "address"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "phone"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "city"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "country"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "job"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "company"))
        )

        # Цвета полей
        zip_code_field = self.driver.find_element(By.NAME, "zipcode")
        assert "red" in zip_code_field.get_attribute("style"), "Zip code field is not highlighted in red"

        for field_name in ["firstname", "lastname", "address", "email", "phone", "city", "country", "job", "company"]:
            field = self.driver.find_element(By.NAME, field_name)
            assert "green" in field.get_attribute("style"), f"{field_name} field is not highlighted in green"