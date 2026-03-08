from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urban_routes_locators import UrbanRoutesLocators

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
        self.wait = WebDriverWait(driver, 15)

    def enter_from_address(self, address):
        self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.FROM_INPUT)
        ).send_keys(address)

    def enter_to_address(self, address):
        element = self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.TO_INPUT)
        )
        element.send_keys(address)
        import time
        time.sleep(3)

    def click_request_taxi(self):
        button = self.wait.until(
            EC.element_to_be_clickable(UrbanRoutesLocators.REQUEST_TAXI_BUTTON)
        )
        button.click()


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
        import time
        time.sleep(5)  #  esperar a que llegue el código

        code= retrieve_phone_code(self.driver)

        # escribir código
        self.driver.find_element(*UrbanRoutesLocators.PHONE_CODE_INPUT).send_keys(code)

        # confirmar
        self.driver.find_element(*UrbanRoutesLocators.PHONE_CONFIRM_BUTTON).click()

    def open_payment_method(self):

        # Espera hasta 20 segundos a que el botón esté clickeable
        payment = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(UrbanRoutesLocators.PAYMENT_METHOD)
        )

        #Asegurar que el elemento este dentro de la pantalla
        self.driver.execute_script("arguments[0].scrollIntoView(true);", payment)
        #Forzar click
        self.driver.execute_script("arguments[0].click();", payment)

        print("Click en metodo de pago")

    def add_card(self, card_number, card_code):

        #Esperar click en agregar tarjeta
        add_card_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(UrbanRoutesLocators.ADD_CARD_BUTTON)
        )

        # Hacer scroll para que sea visible
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_card_button)

        # Click seguro con JS (evita overlays o animaciones)
        self.driver.execute_script("arguments[0].click();", add_card_button)

        # Esperar que aparezcan los inputs del número de tarjeta
        card_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(UrbanRoutesLocators.CARD_NUMBER_INPUT)
        )

        card_input.send_keys(card_number)

        # Código de seguridad
        code_input = self.driver.find_element(*UrbanRoutesLocators.CARD_CODE_INPUT)
        code_input.send_keys(card_code)
            EC.visibility_of_element_located(UrbanRoutesLocators.CARD_NUMBER)
        )
        number_field.send_keys(number)

        code_field = self.wait.until(
            EC.visibility_of_element_located(UrbanRoutesLocators.CARD_CODE)
        )

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