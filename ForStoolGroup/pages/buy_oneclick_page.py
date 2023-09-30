from base.base_class import Base
from pages.product_page import Product_page

PP = Product_page()

class Buy_oneclick_page(Base):

    def __init__(self):
        super().__init__()

    # Locators

    locator_product_name = ["xpath", '//div[contains(@class, "buy-onclick__product-title")]']

    # Methods

    def buy_one_click_and_check_name(self):

        """  Проверяет наименование выбранного товара. """

        value_word = self.asser_word(self.locator_product_name, PP.buy_one_click_button())
        print("___Select product " + value_word + " PASSED")
