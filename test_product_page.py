from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest


link = "https://selenium1py.pythonanywhere.com"

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.base_page = BasePage(browser, link)
        self.login_page = LoginPage(browser, link)
        self.link = self.base_page.url
        self.base_page.open()
        self.base_page.go_to_login_page()
        self.login_page.register_new_user()
        self.base_page.should_be_authorized_user()
        self.base_page.go_to_product_page()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_to_basket()
        page.should_be_add_to_basket_button()
        page.should_be_message_about_adding()
        page.should_be_message_about_product_name()
        page.should_be_message_basket_total()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.guest_cant_see_success_message()    

@pytest.mark.first
@pytest.mark.parametrize('link', link)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_button()
    page.should_be_message_about_product_name()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

@pytest.mark.second
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.second
@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.second
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket()

@pytest.mark.third
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.third  
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.fourth
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
   # page.add_product_to_basket()
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.should_be_text_of_empty_basket()   
    page.should_be_empty_basket()

