from base.base_class import Base
from pages.tables_page import Tables_page

TP = Tables_page()


class Product_page(Base):

    def __init__(self):
        super().__init__()

    # Locators

    locator_product_name = ["xpath", '//h1[contains(@class, "product-interface__title")]']
    locator_product_buy_button = ["xpath", '//div[contains(@class, "product-interface__footer")]'
                                           '//div[contains(text(), "Добавить в корзину")]']
    locator_buy_one_click_button = ["xpath", '//div[contains(@class, "product-interface__footer")]'
                                             '//a[contains(text(), "Купить в один клик")]']

    # Getters

    def get_name_product(self):
        return self.get_text(self.locator_product_name)

    # Actions

    def click_product_buy_button(self):
        self.click_clickable_element(self.locator_product_buy_button)
        print("___Click Button 'Добавить в корзину'")

    def click_buy_one_click_button(self):
        self.click_clickable_element(self.locator_buy_one_click_button)
        print("___Click Button 'Купить в один клик'")

    # Methods

    def open_page_and_check_name(self):

        """  Проверяет наименование выбранного товара. """

        value_word = self.asser_word(self.locator_product_name, TP.open_page_second_product())
        print("___Opened page product " + value_word + " PASSED")

    def add_product_in_cart(self):

        """  Добавление товара в корзину, с помощью кнопки - Добавить в корзину. Возвращает наименование товара. """

        name_before = self.get_name_product()
        self.click_product_buy_button()
        return name_before

    def buy_one_click_button(self):

        """  Выбор товара, с помощью кнопки - Купить в один клик. Возвращает наименование товара. """

        name_before = self.get_name_product()
        self.click_buy_one_click_button()
        return name_before
