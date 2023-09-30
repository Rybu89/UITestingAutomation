from base.base_class import Base
from pages.buy_oneclick_page import Buy_oneclick_page
from pages.cart_page import Cart_page
from pages.product_page import Product_page
from pages.tables_page import Tables_page

TP = Tables_page()
base = Base()
PP = Product_page()
CP = Cart_page()
BoP = Buy_oneclick_page()

def test_add_from_products_page(from_test_add_products_in_cart):

    """ Добавление товара в корзину со страницы с товарами. """

    base.load_cookies('select_products')
    TP.select_first_product_buy_button()
    base.load_cookies('select_products')
    TP.select_first_product_buy_one_click_button()

def test_add_from_product_page(from_test_add_products_in_cart):

    """ Добавление товара в корзину со страницы товара. """

    base.load_cookies('select_products')
    PP.open_page_and_check_name()
    CP.add_product_in_cart_and_check_name()
    base.load_cookies('select_products')
    PP.open_page_and_check_name()
    BoP.buy_one_click_and_check_name()
