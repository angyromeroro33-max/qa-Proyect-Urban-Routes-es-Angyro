from selenium.webdriver.common.by import By


class UrbanRoutesLocators:

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    CALL_TAXI_BUTTON = (By.CSS_SELECTOR, "button.button.round")

    COMFORT_TARIFF = (By.XPATH, "//div[text()='Comfort']")

    PHONE_FIELD = (By.ID, "phone")

    ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Agregar tarjeta']")
    CARD_NUMBER = (By.ID, "number")
    CARD_CODE = (By.ID, "code")
    LINK_CARD_BUTTON = (By.XPATH, "//button[text()='Link']")

    MESSAGE_FIELD = (By.ID, "comment")

    BLANKET_CHECKBOX = (By.XPATH, "//span[text()='Manta y pañuelos']")

    ICECREAM_PLUS = (By.XPATH, "//div[@class='counter-plus']")

    ORDER_TAXI_BUTTON = (By.XPATH, "//button[text()='Pedir taxi']")

    DRIVER_MODAL = (By.CLASS_NAME, "order-details")