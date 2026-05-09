import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UrbanRoutesPage import UrbanRoutesPage
from data import UrbanRoutesData


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()
        cls.driver.get(UrbanRoutesData.URL)

        cls.page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


    def test_set_route(self):

        self.page.enter_from_address(UrbanRoutesData.FROM_ADDRESS)
        self.page.enter_to_address(UrbanRoutesData.TO_ADDRESS)

        # ASSERT dirección origen
        assert self.driver.find_element(By.ID, "from").get_attribute("value") == UrbanRoutesData.FROM_ADDRESS

        self.page.click_request_taxi()


    def test_select_comfort(self):

        self.page.select_comfort()

        # ASSERT tarifa Comfort visible
        assert self.driver.find_element(By.XPATH, "//div[text()='Comfort']").is_displayed()


    def test_fill_phone(self):

        self.page.add_phone_number(UrbanRoutesData.PHONE_NUMBER)

        # ASSERT teléfono aparece
        assert self.driver.find_element(By.XPATH, "//div[contains(@class,'np-text')]").text == UrbanRoutesData.PHONE_NUMBER


    def test_payment_method(self):

        self.page.open_payment_method()

        # ASSERT botón método de pago visible
        btn_pago = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'pp-text')]"))
        )

        assert btn_pago.is_displayed()


    def test_add_card(self):

        self.page.add_card(
            UrbanRoutesData.CARD_NUMBER,
            UrbanRoutesData.CARD_CODE
        )

        self.page.click_card_area()
        self.page.close_card_window()


    def test_driver_message(self):

        self.page.add_message_for_driver("Por favor trae pañuelos")

        # ASSERT mensaje guardado
        assert self.driver.find_element(By.ID, "comment").get_attribute("value") == "Por favor trae pañuelos"


    def test_blanket_switch(self):

        self.page.activate_blanket_switch()

        # ASSERT switch activado
        assert self.driver.find_element(By.CLASS_NAME, "switch-input").is_selected()


    def test_add_ice_cream(self):

        self.page.add_two_ice_creams()


    def test_order_taxi(self):

        self.page.order_taxi()


    def test_wait_driver(self):

        WebDriverWait(self.driver, 60).until_not(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "order-header-content"),
                "Buscar automóvil"
            )
        )

        assert self.driver.find_element(By.CLASS_NAME, "order-header-content").is_displayed()