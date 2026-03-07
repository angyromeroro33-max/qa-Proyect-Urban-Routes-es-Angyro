from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urban_routes_locators import UrbanRoutesLocators


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_from_address(self, address):
        self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.FROM_INPUT)
        ).send_keys(address)

    def enter_to_address(self, address):
        self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.TO_INPUT)
        ).send_keys(address)

    def click_request_taxi(self):
        self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.REQUEST_TAXI_BUTTON)
        ).click()

    def select_personal(self):
        self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.PERSONAL_BUTTON)
        ).click()

    def select_comfort(self):
        self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.COMFORT_TARIFF)
        ).click()

    def get_results_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.RESULTS_TEXT)
        ).text

    def add_phone_number(self, phone_number):
        # abrir ventana teléfono
        self.driver.find_element(*UrbanRoutesLocators.PHONE_BUTTON).click()

        # esperar a que aparezca el campo
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(UrbanRoutesLocators.PHONE_INPUT)
        )
        # Escribir el telefono
        self.driver.find_element(*UrbanRoutesLocators.PHONE_INPUT).send_keys(phone_number)

        # clic en siguiente
        self.driver.find_element(*UrbanRoutesLocators.PHONE_NEXT_BUTTON).click()

        # escribir código
        self.driver.find_element(*UrbanRoutesLocators.PHONE_CODE_INPUT).send_keys("1234")

        # confirmar
        self.driver.find_element(*UrbanRoutesLocators.PHONE_CONFIRM_BUTTON).click()

    def open_payment_method(self):
        self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.PAYMENT_METHOD)
        ).click()

    def add_card(self, number, code):
        self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.ADD_CARD_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.CARD_NUMBER)
        ).send_keys(number)

        code_field = self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.CARD_CODE)
        )

        code_field.send_keys(code)

        code_field.send_keys("\t")

    def close_card_window(self):
        self.wait.until(
            EC.element_to_be_clickable(
                UrbanRoutesLocators.CLOSE_CARD_WINDOW
            )
        ).click()

    def add_message_for_driver(self, message):
        self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.MESSAGE_DRIVER)
        ).send_keys(message)

    def request_blanket_tissues(self):
        self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.BLANKET_TISSUES)
        ).click()

    def add_icecream(self):
        plus = self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.ICECREAM_PLUS)
        )

        plus.click()
        plus.click()

    def final_order(self):
        self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.FINAL_ORDER_BUTTON)
        ).click()