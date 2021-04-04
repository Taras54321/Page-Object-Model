from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest


link = "https://selenium1py.pythonanywhere.com"
link1 = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link2 = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user()
        main_page.should_be_authorized_user()
        main_page.go_to_product_page()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, browser.current_url)
        page.open()
        page.add_product_to_basket()
        page.should_be_add_to_basket_button()
        page.should_be_message_about_adding()
        page.should_be_message_about_product_name()
        page.should_be_message_basket_total()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, browser.current_url)
        page.open()
        page.guest_cant_see_success_message()

@pytest.mark.first
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link2)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_button()
    page.should_be_message_about_adding()
    page.should_be_message_about_product_name()
    page.should_be_message_basket_total()

@pytest.mark.second
# @pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.add_product_to_basket()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.second
# @pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.second
# @pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket()

@pytest.mark.third
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_be_login_link()
  
@pytest.mark.third
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.go_to_login_page()

@pytest.mark.fourth
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link1)
    page.open()
    #page.add_product_to_basket()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_text_of_empty_basket()
    page.should_be_empty_basket()

