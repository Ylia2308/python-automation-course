import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSauceDemo:
    def test_checkout_process(self, driver):

        # Авторизация
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, ".btn_action").click()

        # Добавление товаров в корзину
        self.add_to_cart(driver, "Sauce Labs Backpack")
        self.add_to_cart(driver, "Sauce Labs Bolt T-Shirt")
        self.add_to_cart(driver, "Sauce Labs Onesie")

        # Переход в корзину и оформление заказа
        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        driver.find_element(By.CSS_SELECTOR, ".btn_action.checkout_button").click()

        # Заполнение формы
        self.fill_checkout_form(driver, "Юлия", "Алексеенко", "610035")
        driver.find_element(By.CSS_SELECTOR, ".btn_primary.cart_button").click()

        # Ожидание
        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        total_text = total_element.text
        assert total_text == "Total: $58.29", f"Ожидалось, что итоговая сумма будет '$58.29', но получено '{total_text}'"

   def add_to_cart(self, driver, item_name):
        
        item_selector = f"//div[text()='{item_name}']/ancestor::div[contains(@class, 'inventory_item')]//button"
        driver.find_element(By.XPATH, item_selector).click()

   def fill_checkout_form(self, driver, first_name, last_name, postal_code):
    
        driver.find_element(By.ID, "first-name").send_keys(first_name)
        driver.find_element(By.ID, "last-name").send_keys(last_name)
        driver.find_element(By.ID, "postal-code").send_keys(postal_code)  