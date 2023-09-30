import time

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.main_page import Main_page
from pages.quick_filters_for_furniture import Quick_filters_for_furniture
from pages.tables_page import Tables_page

TP = Tables_page()
ChP = Checkout_page()
Qff = Quick_filters_for_furniture()
base = Base()
MP = Main_page()
CP = Cart_page()

def test_smoke_test(from_module):
    """    Проверка, быстрого фильтра на странице "Столы". """

    # Проверка, быстрого фильтра на странице "Столы".
    base.open_page(MP.url)
    MP.click_and_check_tables_button()
    Qff.select_price_tables_scroll()
    Qff.select_quick_filters_in_stock()
    Qff.select_quick_filters_category_tables()
    Qff.select_quick_filters_brand_stool_group()
    Qff.select_quick_filters_color_walnut()
    base.save_cookies('select_products')

    # Добавление товара в корзину.
    time.sleep(3)
    TP.select_first_product_buy_button()
    base.save_cookies('order_products_1')
    base.load_cookies('select_products')
    TP.select_first_product_buy_one_click_button()

    # Оформление заказа.
    base.load_cookies('order_products_1')
    TP.click_cart()
    CP.click_checkout_button()
    ChP.add_contact_information()
    ChP.select_self_delivery_method()
    ChP.select_private_person_entity()
    ChP.select_online_payment()
    ChP.select_promo_code()
    ChP.click_apply_button()
