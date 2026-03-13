from selenium.webdriver.common.by import By


class UrbanRoutesLocators:

    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")

    REQUEST_TAXI_BUTTON = (By.XPATH, "//button[text()='Pedir un taxi']")

    COMFORT_TARIFF = (By.XPATH, "//div[text()='Comfort']")

    PHONE_BUTTON = (By.XPATH,"//div[contains(@class,'np-text')]")

    PHONE_INPUT = (By.ID, "phone")

    NEXT_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Siguiente']")

    CODE_INPUT = (By.ID, "code")

    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirmar']")

    # Método de pago / tarjeta
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[contains(@class,'pp-text') and text()='Método de pago']")
    ADD_CARD_BUTTON_CONTAINER = (By.XPATH, "//div[text()='Agregar tarjeta']")  # Contenedor para abrir input
    CARD_NUMBER_INPUT = (By.ID, "number")  # input para el número de tarjeta
    CARD_CODE_INPUT = (By.XPATH, "//input[@id='code' and contains(@class,'card-input')]") # input para el código de seguridad de la tarjeta
    CARD_AREA = (By.CLASS_NAME,"card-wrapper")
    SUBMIT_CARD_BUTTON = (By.XPATH, "//button[text()='Agregar' and not(contains(@class,'disabled'))]")  # botón agregar
    CLOSE_BUTTON = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')


    MESSAGE_FOR_DRIVER_INPUT = (By.ID, "comment")
    #Extras
    BLANKET_TISSUES_SWITCH = (By.CLASS_NAME, 'switch-input')

    ICE_CREAM_PLUS = (By.CSS_SELECTOR, ".counter-plus")


    ORDER_TAXI_BUTTON = (By.XPATH, "//button[.//span[text()='Pedir un taxi']]")

    DRIVER_INFO_MODAL = (By.CLASS_NAME, 'order-btn-group')

    DETAILS_BUTTON = (By.XPATH, "//div[@class='order-btn-group'][3]")