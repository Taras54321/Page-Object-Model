from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-block")
    PRODUCT_LINK = (By.CSS_SELECTOR, "li ul > li a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "a.btn-lg")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h3 a")   
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

