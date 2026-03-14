import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UrbanRoutesPage import UrbanRoutesPage
from data import UrbanRoutesData


@pytest.fixture
def driver():
    options = Options()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(UrbanRoutesData.URL)

    yield driver
    driver.quit()


def test_complete_taxi_order(driver):

    page = UrbanRoutesPage(driver)

    page.enter_from_address(UrbanRoutesData.FROM_ADDRESS)
    page.enter_to_address(UrbanRoutesData.TO_ADDRESS)
    # ASSERT dirección origen
    assert driver.find_element(By.ID, "from").get_attribute("value") == UrbanRoutesData.FROM_ADDRESS

    page.click_request_taxi()

    page.select_comfort()
    # ASSERT tarifa Comfort visible
    assert driver.find_element(By.XPATH, "//div[text()='Comfort']").is_displayed()

    # escribir teléfono
    page.add_phone_number(UrbanRoutesData.PHONE_NUMBER)
    # ASSERT teléfono aparece en pantalla
    assert driver.find_element(By.XPATH, "//div[contains(@class,'np-text')]").text == UrbanRoutesData.PHONE_NUMBER

    page.open_payment_method()

    page.add_card(
        UrbanRoutesData.CARD_NUMBER,
        UrbanRoutesData.CARD_CODE
    )
    # ASSERT botón método de pago visible
    btn_pago = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'pp-text')]"))
    )
    assert btn_pago.is_displayed()

    page.click_card_area()

    page.close_card_window()

    page.add_message_for_driver("Por favor trae pañuelos")
    # ASSERT mensaje guardado
    assert driver.find_element(By.ID, "comment").get_attribute("value") == "Por favor trae pañuelos"

    page.activate_blanket_switch()
    # ASSERT switch activado
    assert driver.find_element(By.CLASS_NAME, "switch-input").is_selected()

    page.add_two_ice_creams()

    page.order_taxi()

    #esperar al conductor
    WebDriverWait(driver, 60).until_not(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "order-header-content"), "Buscar automóvil")
    )

    assert driver.find_element(By.CLASS_NAME, "order-header-content").is_displayed()

