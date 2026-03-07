from selenium.webdriver.common.by import By


class UrbanRoutesLocators:
    # Campos de dirección
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")

    # Botón pedir taxi
    REQUEST_TAXI_BUTTON = (By.XPATH, "//button[contains(text(),'Pedir un taxi')]")

    # Botón Personal
    PERSONAL_BUTTON = (By.XPATH, "//div[contains(text(),'Personal')]")

    # Tarifa Comfort
    COMFORT_TARIFF = (By.XPATH, "//div[contains(text(),'Comfort')]")

    # Texto resultado taxi
    RESULTS_TEXT = (By.CLASS_NAME, "results-text")

    # Teléfono
    PHONE_BUTTON = (By.XPATH, "//div[text()='Número de teléfono']")
    PHONE_INPUT = (By.ID, "phone")
    PHONE_NEXT_BUTTON = (By.XPATH, "//button[text()='Siguiente']")

    PHONE_CODE_INPUT = (By.ID, "code")
    PHONE_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirmar']")

    # Método de pago
    PAYMENT_METHOD = (By.XPATH, "//div[text()='Método de pago']")

    # Agregar tarjeta
    ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Agregar tarjeta']")
    CARD_NUMBER = (By.ID, "number")
    CARD_CODE = (By.ID, "code")

    PHONE_CODE_INPUT = (By.ID, "code")
    PHONE_CODE_INPUT = (By.ID, "code")

    PHONE_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirmar']")

    # Método de pago
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[text()='Método de pago']")

    # Agregar tarjeta
    ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Agregar tarjeta']")
    CARD_NUMBER = (By.ID, "number")
    CARD_CODE = (By.ID, "code")

    # Mensaje al conductor
    MESSAGE_DRIVER = (By.ID, "comment")

    # Manta y pañuelos
    BLANKET_TISSUES = (By.XPATH, "//div[text()='Manta y pañuelos']/following::input[1]")

    # Helado
    ICECREAM_PLUS = (By.XPATH, "//div[text()='Helado']/following::div[contains(@class,'counter-plus')]")

    # Botón final
    FINAL_ORDER_BUTTON = (By.CLASS_NAME, "smart-button")
