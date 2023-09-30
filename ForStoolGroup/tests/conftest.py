import time

import pytest

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.tables_page import Tables_page

base = Base()
MP = Main_page()
TP = Tables_page()
CP = Cart_page()

@pytest.fixture(scope="module")
def from_module():

    """ Очистка куков перед запуском тестов. Запрос на удаление скриншотов, после прогона. """

    print('\nSTART')
    base.browser.delete_all_cookies()

    yield
    base.deleting_all_screenshots()
    time.sleep(5)
    base.browser.quit()
    print('\n FINISH')

@pytest.fixture()
def from_test_quick_filters():

    """ Подготовка к прогону теста quick_filters_for_furniture. Сохранение куков, после прогона. """

    print('\n Start test')
    base.open_page(MP.url)
    MP.click_and_check_tables_button()

    yield
    base.save_cookies('select_products')
    print('\n Finish test')

@pytest.fixture()
def from_test_add_products_in_cart():

    """ Подготовка к прогону теста test_add_products_in_cart. """

    print('\n Start test')
    base.open_page("https://stoolgroup.ru/stoly/?features_hash=21-275_72-7048_81-14283_102-11927-83135-RUB_135-Y")

    yield
    print('\n Finish test')

@pytest.fixture()
def from_test_place_orders():

    """ Подготовка к прогону теста 03. """

    print('\n Start test')
    base.open_page("https://stoolgroup.ru/stoly/?features_hash=21-275_72-7048_81-14283_102-11927-83135-RUB_135-Y")
    base.load_cookies('order')
    TP.click_cart()
    CP.click_checkout_button()

    yield
    print('\n Finish test')
