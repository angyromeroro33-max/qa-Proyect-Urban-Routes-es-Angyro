from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urban_routes_locators import UrbanRoutesLocators


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_route(self, from_address, to_address):
        self.driver.find_element(*UrbanRoutesLocators.FROM_FIELD).send_keys(from_address)
        self.driver.find_element(*UrbanRoutesLocators.TO_FIELD).send_keys(to_address)

    def click_call_taxi(self):
        self.driver.find_element(*UrbanRoutesLocators.CALL_TAXI_BUTTON).click()

    def select_comfort(self):
        self.driver.find_element(*UrbanRoutesLocators.COMFORT_TARIFF).click()

    def set_phone(self, phone):
        self.driver.find_element(*UrbanRoutesLocators.PHONE_FIELD).send_keys(phone)

    def add_card(self, number, code):
        self.driver.find_element(*UrbanRoutesLocators.ADD_CARD_BUTTON).click()
        self.driver.find_element(*UrbanRoutesLocators.CARD_NUMBER).send_keys(number)
        code_field = self.driver.find_element(*UrbanRoutesLocators.CARD_CODE)
        code_field.send_keys(code)
        code_field.send_keys(Keys.TAB)
        self.driver.find_element(*UrbanRoutesLocators.LINK_CARD_BUTTON).click()

    def write_message(self, message):
        self.driver.find_element(*UrbanRoutesLocators.MESSAGE_FIELD).send_keys(message)

    def request_blanket(self):
        self.driver.find_element(*UrbanRoutesLocators.BLANKET_CHECKBOX).click()

    def add_icecream(self, amount):
        for _ in range(amount):
            self.driver.find_element(*UrbanRoutesLocators.ICECREAM_PLUS).click()

    def order_taxi(self):
        self.driver.find_element(*UrbanRoutesLocators.ORDER_TAXI_BUTTON).click()

    def wait_for_driver(self):
        self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.DRIVER_MODAL)
        )