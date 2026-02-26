from selenium.webdriver.common.by import By


class UrbanRoutesLocators:

    # ========= DIRECCIONES =========
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")

    # ========= TARIFA =========
    COMFORT_TARIFF = (By.XPATH, "//div[text()='Comfort']")

    # ========= TELÉFONO =========
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON_PHONE = (By.XPATH, "//button[text()='Siguiente']")

    # ========= AGREGAR TARJETA =========
    ADD_CARD_BUTTON = (By.XPATH, "//button[text()='Agregar tarjeta']")
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CVV_INPUT = (By.ID, "code")
    LINK_CARD_BUTTON = (By.XPATH, "//button[text()='Vincular']")

    # ========= MENSAJE AL CONDUCTOR =========
    MESSAGE_INPUT = (By.ID, "comment")

    # ========= MANTA Y PAÑUELOS =========
    BLANKET_TISSUES_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @name='blanket']")

    # ========= HELADOS =========
    ICE_CREAM_PLUS_BUTTON = (By.XPATH, "//button[@data-test='icecream-plus']")

    # ========= PEDIR TAXI =========
    ORDER_TAXI_BUTTON = (By.XPATH, "//button[text()='Pedir taxi']")

    # ========= MODAL BUSCANDO TAXI =========
    SEARCHING_MODAL = (By.CLASS_NAME, "order-header")

    # ========= INFORMACIÓN DEL CONDUCTOR (PASO OPCIONAL) =========
    DRIVER_INFO_MODAL = (By.CLASS_NAME, "order-details")