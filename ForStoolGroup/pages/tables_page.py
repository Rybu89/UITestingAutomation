from base.base_class import Base


class Tables_page(Base):

    def __init__(self):
        super().__init__()

    # Test data

    url = 'https://stoolgroup.ru/stoly/'

    # Locators

    locator_page_title = ["xpath", '//h1[@data-only-title="title"]']
    value_locator_page_title = 'Столы'

    # products
    locator_second_product_image = ["xpath", '(//div[@class="product-card__img-wrapper"])[2]']
    locator_second_product_name = ["xpath", '(//div[@class="product-card__title"])[2]']
    locator_first_product_buy_button = ["xpath", '(//a[contains(@class, "button-buy")])[1]']
    locator_first_product_name = ["xpath", '(//div[@class="product-card__title"])[1]']
    locator_first_product_name_in_cart = ["xpath", '(//a[@class="product-preview__descr"])[1]']
    locator_cart = ["xpath", '//div[@id="cart_amount"]']
    locator_cart_title = ["xpath", '//div[@class="cart-preview__title" and contains(text(), "Ваша корзина")]']
    locator_first_product_buy_one_click_button = ["xpath", '(//a[contains(@class, "product-card__buy")])[1]']
    locator_first_product_name_in_order = ["xpath", '//div[contains(@class, "buy-onclick__product-title")]']

    # Getters

    def get_name_first_product(self):
        return self.get_text(self.locator_first_product_name)

    def get_name_first_product_in_cart(self):
        return self.get_text(self.locator_first_product_name_in_cart)

    def get_name_first_product_in_order(self):
        return self.get_text(self.locator_first_product_name_in_order)

    def get_name_second_product(self):
        return self.get_text(self.locator_second_product_name)

    # Actions

    def click_first_product_buy_button(self):
        self.click_clickable_element(self.locator_first_product_buy_button)
        print("___Click Button 'Купить'")

    def click_first_product_buy_one_click_button(self):
        self.click_clickable_element(self.locator_first_product_buy_one_click_button)
        print("___Click Button 'Купить в один клик'")

    def click_cart(self):
        self.click_visibility_element(self.locator_cart)
        value_title = self.asser_word(self.locator_cart_title, "Ваша корзина")
        print("___Click Button 'Cart'. Page title after clicking: " + value_title + " PASSED")

    def click_second_product_image(self):
        self.click_clickable_element(self.locator_second_product_image)
        print("___Click on image second product.")

    # Methods

    def select_first_product_buy_button(self):

        """  Добавление первого в списке товара в корзину, с помощью кнопки - Купить.
         Добавление товара в корзину, переход в корзину, проверка по наименованию товара. """

        name_before = self.get_name_first_product()
        self.move_to_element(self.locator_first_product_name)
        self.click_first_product_buy_button()
        self.click_cart()
        name_after = self.get_name_first_product_in_cart()
        assert name_before == name_after
        print("___Select product " + name_after + " PASSED")
        # self.save_cookies('order_products_1')

    def select_first_product_buy_one_click_button(self):

        """  Добавление первого в списке товара в корзину, с помощью кнопки - Купить в один клик.
         Добавление товара в корзину, переход в корзину, проверка по наименованию товара. """

        # self.load_cookies('select_products')
        name_before = self.get_name_first_product()
        self.move_to_element(self.locator_first_product_name)
        self.click_first_product_buy_one_click_button()
        name_after = self.get_name_first_product_in_order()
        assert name_before == name_after
        print("___Select product " + name_after + " PASSED")

    def open_page_second_product(self):

        """  Открытие страницы товара, с помощью клика по его изображению. Возвращает наименование товара.
         Клик по изображению, переход на страницу. """

        name_before = self.get_name_second_product()
        self.click_second_product_image()
        return name_before
