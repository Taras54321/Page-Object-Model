from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


link = "https://selenium1py.pythonanywhere.com"

@pytest.mark.first
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
   
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    
@pytest.mark.second
def test_url_need_to_be_correct(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

@pytest.mark.second    
def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

@pytest.mark.second   
def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

@pytest.mark.fourth    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
   # page.add_product_to_basket()
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.should_be_text_of_empty_basket()
    page.should_be_empty_basket()

