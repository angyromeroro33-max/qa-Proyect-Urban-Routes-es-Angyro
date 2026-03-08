import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urban_routes_page import UrbanRoutesPage
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

    page.click_request_taxi()

    page.select_comfort()

    # escribir teléfono
    page.add_phone_number(UrbanRoutesData.PHONE_NUMBER)

    page.open_payment_method()

    page.add_card(
        UrbanRoutesData.CARD_NUMBER,
        UrbanRoutesData.CARD_CODE
    )
    page.close_card_window()

    page.add_message_for_driver(
        UrbanRoutesData.MESSAGE_FOR_DRIVER
    )

    page.request_blanket_tissues()

    page.add_icecream()

    page.final_order()
