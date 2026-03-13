from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UrbanRoutesLocators import UrbanRoutesLocators

def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def enter_from_address(self, address):
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.FROM_INPUT)).send_keys(address)

    def enter_to_address(self, address):
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.TO_INPUT)).send_keys(address)

    def click_request_taxi(self):
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.REQUEST_TAXI_BUTTON)).click()

    def select_comfort(self):
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.COMFORT_TARIFF)).click()

    def add_phone_number(self, phone):
        #Abrir ventana de teléfono
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.PHONE_BUTTON)).click()

        #Escribir el número
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.PHONE_INPUT)).send_keys(phone)

        #Hacer click en el botón siguiente
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.NEXT_BUTTON)).click()

        #Esperar a que aparezca el SMS
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.CODE_INPUT))

        # Espera extra para que el código llegue a los logs
        import time
        time.sleep(2)

        #Obtener el código SMS automáticamente
        Code = retrieve_phone_code(self.driver)

        # escribir el código
        self.driver.find_element(*UrbanRoutesLocators.CODE_INPUT).send_keys(Code)

        #confirmar
        confirm_btn = self.driver.find_element(*UrbanRoutesLocators.CONFIRM_BUTTON)
        self.driver.execute_script("arguments[0].click();", confirm_btn)

    def open_payment_method(self):
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.PAYMENT_METHOD_BUTTON)).click()

    def add_card(self, number, code):
        # Clic en contenedor "Agregar tarjeta"
        self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.ADD_CARD_BUTTON_CONTAINER)).click()

        # Escribir número de tarjeta
        card_element = self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.CARD_NUMBER_INPUT)).send_keys(
            number)

        # Escribir código de seguridad
        cvv_element = self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.CARD_CODE_INPUT)
        )
        cvv_element.clear()
        cvv_element.send_keys(code)

    def click_code_field(self, locators=None):
        code_field = self.wait.until(
            EC.element_to_be_clickable(self.locators.CODE_FIELD)
        )
        code_field.click()

    def click_card_area(self):
        self.wait.until(
                EC.element_to_be_clickable(UrbanRoutesLocators.CARD_AREA)
            ).click()
        self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.CARD_AREA)
        ).click()

        # Click en botón Agregar
        submit_btn = self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.SUBMIT_CARD_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", submit_btn)

    def close_card_window(self):
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.CLOSE_BUTTON)).click()

    def add_message_for_driver(self, message):
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.MESSAGE_FOR_DRIVER_INPUT)).send_keys(message)

    def activate_blanket_switch(self):
        wait = WebDriverWait(self.driver, 10)

        # Espera a que el switch esté clickeable
        blanket_switch = wait.until(
            EC.presence_of_element_located(UrbanRoutesLocators.BLANKET_TISSUES_SWITCH)
    )

    # Hacer scroll para asegurarse que sea visible
        self.driver.execute_script("arguments[0].scrollIntoView();", blanket_switch)

    # Hacer clic con JavaScript
        self.driver.execute_script("arguments[0].click();", blanket_switch)

    def add_two_ice_creams(self):

        plus_button = self.wait.until(
        EC.element_to_be_clickable(UrbanRoutesLocators.ICE_CREAM_PLUS)
        )

        # click 1
        plus_button.click()

        # click 2
        plus_button.click()

    def order_taxi(self):
        order_button = self.wait.until(
        EC.element_to_be_clickable(UrbanRoutesLocators.ORDER_TAXI_BUTTON)
        )
        order_button.click()
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.DETAILS_BUTTON)).click()