from pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

#@pytest.mark.parametrize('link', link)
#def test_guest_can_add_product_to_basket(browser, link):
    #page = ProductPage(browser, link)
    #page.open()
    #page.add_product_to_basket()
    #page.solve_quiz_and_get_code()
    #page.should_be_add_to_basket_button()
    #page.should_be_message_about_product_name()
    #page.should_be_message_about_adding()
    #page.should_be_message_basket_total()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket()

