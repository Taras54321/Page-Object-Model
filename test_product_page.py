from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_button()
    page.should_be_message_about_product_name()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
