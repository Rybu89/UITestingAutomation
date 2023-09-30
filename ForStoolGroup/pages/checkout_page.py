import time

from selenium.webdriver import ActionChains, Keys

from base.base_class import Base


class Checkout_page(Base):

    def __init__(self):
        super().__init__()

    # Test data

    first_name = 'Иван'
    last_name = 'Иванов'
    email = 'xxx@mail.ru'
    phone = '9001234567'
    promo_code = '12345'
    delivery_address = 'Москва, Краснопресненская набережная, 2'
    confirmation_value = ['Товар', 'Артикул', 'Цена за шт.', 'Количество', 'Общая цена']

    # Locators
    locator_contact_information_title = ['xpath', '(//div[@class="cart-form__item-title"])[1]']
    locator_first_name_field = ['xpath', '//input[@id="firstname"]']
    locator_last_name_field = ['xpath', '//input[@id="lastname"]']
    locator_email_field = ['xpath', '//input[@id="email"]']
    locator_phone_field = ['xpath', '//input[@id="phone"]']

    locator_delivery_address_title = ['xpath', '(//div[@class="cart-form__item-title"])[2]']
    locator_address1 = ['xpath', '//input[@id="s_address"]']
    locator_address2 = ['xpath', '//input[@id="s_house"]']

    locator_delivery_method = ['xpath', '(//div[@class="cart-form__item-title"])[3]']
    locator_delivery_title = ['xpath', '(//div[@id="shipping_rates_list"]//div[@class="radiobtn__title"])[1]']
    locator_self_delivery_radio_button = ['xpath', '//input[@id="sh_0_11"]']
    locator_self_delivery_title = ['xpath', '(//div[@id="shipping_rates_list"]//div[@class="radiobtn__title"])[2]']
    locator_delivery_radio_button = ['xpath', '//input[@id="sh_0_12"]']

    locator_private_person_radio_button = ['xpath', '//div[@id="title_tab1"]']
    locator_online_payment_radio_button = ['xpath', '//input[@id="radio_28"]']
    locator_online_payment_title = ['xpath', '(//div[@class="tab-content"]//div[@class="radiobtn__info"])[1]']
    locator_payment_upon_receipt_radio_button = ['xpath', '//input[@id="radio_19"]']
    locator_payment_upon_receipt_title = ['xpath', '(//div[@class="tab-content"]//p[@class="radiobtn__info-title"])[1]']

    locator_legal_person_radio_button = ['xpath', '//div[@id="title_tab3"]']

    locator_promo_code_title = ['xpath', '(//div[@class="cart-form__item-title"])[4]']
    locator_promo_code_radio_button = ['xpath', '//div[@id="promocode-tab"]']
    locator_promo_code_field = ['xpath', '//input[@id="coupon_field"]']
    locator_bonus_radio_button = ['xpath', '//div[@id="bonuses-tab"]']

    locator_confirmation_title = ['xpath', '(//div[@class="cart-form__item-title"])[5]']
    locator_confirmation_value = ['xpath', '//div[@class="cart-form__item-content"]'
                                           '//div[@class="product-confirm__head"]']

    locator_comment_title = ['xpath', '(//div[@class="cart-form__item-title"])[6]']
    locator_comment_value = ['xpath', '//textarea[@id="comment"]']

    locator_apply_button = ['xpath', '//button[@type="button" and contains(text(), "Применить")]']

    # Actions

    def input_first_name(self):

        """  Ввод в поле - Имя. """

        self.get_present_element(self.locator_first_name_field).clear()
        self.get_present_element(self.locator_first_name_field).send_keys(self.first_name)
        print("___Input first name: " + self.first_name)

    def input_last_name(self):

        """  Ввод в поле - Фамилия. """

        self.get_present_element(self.locator_last_name_field).clear()
        self.get_present_element(self.locator_last_name_field).send_keys(self.last_name)
        print("___Input last name: " + self.last_name)

    def input_email(self):

        """  Ввод в поле - Email. """

        self.get_present_element(self.locator_email_field).clear()
        self.get_present_element(self.locator_email_field).send_keys(self.email)
        print("___Input email: " + self.email)

    def input_phone(self):

        """  Ввод в поле - Телефон. """

        self.get_present_element(self.locator_phone_field).clear()
        self.get_present_element(self.locator_phone_field).send_keys(self.phone)
        print("___Input phone: " + self.phone)

    def input_promo_code(self):

        """  Ввод в поле - Промокод. """

        self.scroll_browser(0, 600)
        self.get_present_element(self.locator_promo_code_field).clear()
        self.get_present_element(self.locator_promo_code_field).send_keys(self.promo_code)
        print("___Input promo-code: " + self.promo_code)

    def click_radio_button_promo_code(self):

        """ Использование промокода """

        try:
            # Проверка и нажатие на кнопку
            value = self.check_and_click_checkbox(self.locator_promo_code_radio_button, 'aria-selected', 'true')

        except:
            # На случай если промокод выбран, но по умолчанию имеет значение aria-selected = false """
            self.click_clickable_element(self.locator_bonus_radio_button)
            value = self.check_and_click_checkbox(self.locator_promo_code_radio_button, 'aria-selected', 'true')

        print("___Click Checkbox 'Промокод'. Status before click: " + value[0] + "." + " Status after click: "
              + value[1] + "." + " Check PASSED")

    def click_apply_button(self):

        """  Клик по кнопке - Применить. """

        self.click_clickable_element(self.locator_apply_button)
        print("___Click Button 'Применить'")
        self.screenshot("click_apply_button")

    def select_self_delivery_method(self):

        """ Выбор способа доставки - Самовывоз. Проверка и нажатие на чек-бокс Самовывоз. """

        self.scroll_browser(0, 600)
        value = self.check_and_click_checkbox(self.locator_self_delivery_radio_button, 'checked', 'true')
        print("___Click Checkbox 'Самовывоз  по адресу  — 15 км от МКАД по М10'. Status before click: " +
              value[0] + "." + " Status after click: " + value[1] + "." + " Check PASSED")
        self.screenshot("select_self_delivery_method")

    def select_legal_person_entity(self):

        """ Выбор Юридического лица. Проверка и нажатие на чек-бокс Юридическое лицо. """

        value = self.check_and_click_checkbox(self.locator_legal_person_radio_button, 'aria-selected', 'true')
        print("___Click Checkbox 'Юридическое лицо'. Status before click: " + value[0] + "." + " Status after click: " +
              value[1] + "." + " Check PASSED")

    def select_private_person_entity(self):

        """ Выбор Физического лица. Проверка и нажатие на чек-бокс Физическое лицо. """

        value = self.check_and_click_checkbox(self.locator_private_person_radio_button, 'aria-selected', 'true')
        print("___Click Checkbox 'Физическое лицо'. Status before click: " + value[0] + "." + " Status after click: " +
              value[1] + "." + " Check PASSED")
        self.screenshot("select_private_person_entity")

    def select_online_payment(self):

        """ Выбор способа оплаты - онлайн. Проверка и нажатие на кнопку Онлайн оплата """

        value = self.check_and_click_checkbox(self.locator_online_payment_radio_button, 'checked', 'true')
        print("___Click Checkbox 'Онлайн оплата'. Status before click: " + value[0] + "." + " Status after click: " +
              value[1] + "." + " Check PASSED")
        self.screenshot("select_online_payment")

    def select_promo_code(self):

        """ Добавление промокода. Проверка и нажатие на кнопку Промокод, ввод в поле Промокод. """

        self.click_radio_button_promo_code()
        self.input_promo_code()
        self.screenshot("select_promo_code")

    # Methods

    def add_contact_information(self):

        """ Заполнение раздела 'Контактная информация """

        self.input_first_name()
        self.input_last_name()
        self.input_phone()
        self.input_email()
        self.screenshot('add_contact_information')

    def check_presence_of_parameter_contact_information(self):

        """ Проверка наличия раздела Контактная информация и полей ввода в разделе (Имя, Фамилия, E-mail, Телефон). """

        value_contact_information = self.get_text(self.locator_contact_information_title)
        value_name = self.check_attribute(self.locator_first_name_field, 'placeholder', 'имя')
        value_lastname = self.check_attribute(self.locator_last_name_field, 'placeholder', 'фамилия')
        value_email = self.check_attribute(self.locator_email_field, 'placeholder', 'почта')
        value_phone = self.check_attribute(self.locator_phone_field, 'placeholder', 'Телефон')
        print(f"___Check presence of parameter {value_contact_information} present "
              f"{value_name}, {value_lastname}, {value_email}, {value_phone} PASSED")

    def check_presence_of_parameter_delivery_address(self):

        """ Проверка наличия раздела Адрес доставки и
            полей ввода в разделе (Область / регион, город; Квартира / Офис). """

        value_delivery_address = self.get_text(self.locator_delivery_address_title)
        value_address1 = self.check_attribute(self.locator_address1, 'placeholder', 'Область / регион, город')
        value_address2 = self.check_attribute(self.locator_address2, 'placeholder', 'Квартира / Офис')
        print(f"___Check presence of parameter {value_delivery_address} present "
              f"{value_address1}, {value_address2} PASSED")

    def check_presence_of_parameter_delivery_method(self):

        """ Проверка наличия раздела Способ доставки и кнопок в разделе (Самовывоз, Доставка). """

        self.scroll_browser(0, 600)
        self.get_present_element(self.locator_address1).clear()
        self.get_present_element(self.locator_address1).send_keys(self.delivery_address)
        time.sleep(1)
        self.get_present_element(self.locator_address1).send_keys(Keys.ENTER)
        clickable = self.browser.find_element("xpath", '//div[@id="cart_amount"]')
        ActionChains(self.browser) \
            .move_to_element(clickable) \
            .move_by_offset(20, 20) \
            .click() \
            .perform()
        self.scroll_browser(0, 600)
        value_delivery_method = self.get_text(self.locator_delivery_method)
        value_self_delivery = self.asser_word(self.locator_self_delivery_title, 'Самовывоз')
        time.sleep(1)
        value_delivery = self.asser_word(self.locator_delivery_title, 'Доставка')
        print(f"___Check presence of parameter {value_delivery_method} present "
              f"{value_self_delivery}, {value_delivery} PASSED")

    def check_presence_of_parameter_private_person(self):

        """ Проверка наличия раздела Физическое лицо и кнопок в разделе (Онлайн оплата, Оплата при получении). """

        value_person = self.get_text(self.locator_private_person_radio_button)
        value_online_payment = self.asser_word(self.locator_online_payment_title, 'Онлайн оплата')
        value_payment_upon_receipt = self.asser_word(self.locator_payment_upon_receipt_title, 'при получении')
        print(f"___Check presence of parameter {value_person} present "
              f"{value_online_payment}, {value_payment_upon_receipt} PASSED")

    def check_presence_of_promocode(self):

        """ Проверка наличия раздела Использовать бонусы или промокод и кнопок в разделе (Промокод, Бонусы). """

        value_title = self.get_text(self.locator_promo_code_title)
        value_button1 = self.asser_word(self.locator_promo_code_radio_button, 'Промокод')
        value_button2 = self.asser_word(self.locator_bonus_radio_button, 'Бонусы')
        print(f"___Check presence of parameter {value_title} present {value_button1}, {value_button2} PASSED")

    def check_presence_of_confirmation(self):

        """ Проверка наличия раздела Подтверждение и полей в
            разделе (Товар, Артикул, Цена за шт., Количество, Общая цена). """

        value_title = self.get_text(self.locator_confirmation_title)
        z = 0
        for _ in self.confirmation_value:
            self.asser_word(self.locator_confirmation_value, self.confirmation_value[z])
            z = z + 1
        print(f"___Check presence of parameter {value_title} present "
              f"{self.get_text(self.locator_confirmation_value)} PASSED")

    def check_presence_of_comment(self):

        """ Проверка наличия раздела Комментарий к заказу и поля ввода в разделе (Введите сообщение). """

        value_title = self.get_text(self.locator_comment_title)
        value_comment = self.check_attribute(self.locator_comment_value, 'placeholder', 'Введите сообщение')
        print(f"___Check presence of parameter {value_title} present {value_comment} PASSED")
