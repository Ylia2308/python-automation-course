import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFormSubmission:
    @pytest.fixture(scope="class")
    def setup(self, request):
        driver = webdriver.Edge()
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        request.cls.driver = driver  
        yield
        driver.quit()

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, value))
        )

    def test_form_submission(self, setup):
        self.wait_for_element(By.NAME, "firstname").send_keys("Иван")
        self.wait_for_element(By.NAME, "lastname").send_keys("Петров")
        self.wait_for_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self.wait_for_element(By.NAME, "email").send_keys("test@skypro.com")
        self.wait_for_element(By.NAME, "phone").send_keys("+7985899998787")
        self.wait_for_element(By.NAME, "zipcode").send_keys("") 
        self.wait_for_element(By.NAME, "city").send_keys("Москва")
        self.wait_for_element(By.NAME, "country").send_keys("Россия")
        self.wait_for_element(By.NAME, "job").send_keys("QA")
        self.wait_for_element(By.NAME, "company").send_keys("SkyPro")

        self.wait_for_element(By.XPATH, "//button[text()='Submit']").click()

        
        fields_to_check = [
            "firstname", "lastname", "address", "email", "phone", "city", "country", "job", "company"
        ]

        for field_name in fields_to_check:
            field = self.wait_for_element(By.NAME, field_name)
            assert "green" in field.get_attribute("style"), f"{field_name} field is not highlighted in green"

        zip_code_field = self.wait_for_element(By.NAME, "zipcode")
        assert "red" in zip_code_field.get_attribute("style"), "Zip code field is not highlighted in red"
