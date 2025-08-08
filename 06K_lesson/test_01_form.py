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

        self.wait_for_element(driver, By.NAME, "first-name").send_keys("Иван")
        self.wait_for_element(driver, By.NAME, "last-name").send_keys("Петров")
        self.wait_for_element(driver, By.NAME, "address").send_keys("Ленина, 55-3")
        self.wait_for_element(driver, By.NAME, "e-mail").send_keys("test@skypro.com")
        self.wait_for_element(driver, By.NAME, "phone").send_keys("+7985899998787")
        self.wait_for_element(driver, By.NAME, "zip-code").send_keys("") 
        self.wait_for_element(driver, By.NAME, "city").send_keys("Москва")
        self.wait_for_element(driver, By.NAME, "country").send_keys("Россия")
        self.wait_for_element(driver, By.NAME, "job-position").send_keys("QA")
        self.wait_for_element(driver, By.NAME, "company").send_keys("SkyPro")

        self.wait_for_element(driver, By.XPATH, "//button[text()='Submit']").click()

        fields_to_check = [
            "firstname", "lastname", "address", "email", "phone", "city", "country", "job", "company"
        ]

        for field_name in fields_to_check:
            field = self.wait_for_element(driver, By.NAME, field_name)
            assert "green" in field.get_attribute("style"), f"{field_name} field is not highlighted in green"

        zip_code_field = self.wait_for_element(driver, By.NAME, "zipcode")
        assert "red" in zip_code_field.get_attribute("style"), "Zip code field is not highlighted in red"

    @staticmethod
    def wait_for_element(driver, by, value):
        return WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((by, value))
        )
