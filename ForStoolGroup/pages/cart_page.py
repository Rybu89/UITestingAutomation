from base.base_class import Base
from pages.product_page import Product_page

PP = Product_page()

class Cart_page(Base):

    def __init__(self):
        super().__init__()

    # Locators

    locator_checkout_button = ['xpath', '//a[contains(text(), "Оформить заказ")]']
    locator_first_product_name = ["xpath", '(//a[@class="product-preview__descr"])[1]']

    # Actions

    def click_checkout_button(self):
        """ Переход на страницу Оформление заказа и сохранение cookie """

        self.click_clickable_element(self.locator_checkout_button)
        self.save_cookies('order')
        print("___Click Button 'Оформить заказ'")

    # Methods

    def add_product_in_cart_and_check_name(self):

        """  Проверяет наименование выбранного товара. """

        value_word = self.asser_word(self.locator_first_product_name, PP.add_product_in_cart())
        print("___Select product " + value_word + " PASSED")
