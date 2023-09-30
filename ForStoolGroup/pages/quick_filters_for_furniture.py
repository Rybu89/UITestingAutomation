from base.base_class import Base


class Quick_filters_for_furniture(Base):

    def __init__(self):
        super().__init__()

    # Test data

    step_scroll_filter_price_rang_min = [25, 0]
    step_scroll_filter_price_rang_max = [-50, 0]
    availability_content_quick_filters = ['Диапазон цены', 'В наличии', 'Категория', 'Бренд', 'Цвет']

    # Locators

    locator_quick_filters_price_range = ["xpath",
                                         '//div[@class="spoiler__title" and contains(text(), "Диапазон цены")]']
    locator_quick_filters_price_range_min_scroll = ["xpath", '(//span[contains(@class, "range__identify-btn_low")])[6]']
    locator_quick_filters_price_range_max_scroll = ["xpath", '(//span[contains(@class, "range__identify-btn_up")])[6]']
    locator_quick_filters_price_range_min_input = ["xpath", '//input[@id="slider_116_102_left"]']
    locator_quick_filters_price_range_max_input = ["xpath", '//input[@id="slider_116_102_right"]']

    locator_quick_filters_in_stock_button = ["xpath",
                                             '//div[@class="spoiler__title" and contains(text(), "В наличии")]']
    locator_quick_filters_in_stock_visible_checkbox = ["xpath",
                                                       '(//div[@class="filters-checkbox__info" and contains(text(), '
                                                       '"В наличии")])[2]']
    locator_quick_filters_in_stock_checkbox = ["xpath", '//input[@id="elm_checkbox_116_135_Y"]']
    locator_quick_filters_category_button = ["xpath",
                                             '//div[@class="spoiler__title" and contains(text(), "Категория")]']
    locator_quick_filters_category_visible_checkbox = ["xpath", '(//div[@class="filters-checkbox__info" and '
                                                                'contains(text(), "Столы")])[3]']
    locator_quick_filters_category_checkbox_tables = ["xpath", '//input[@id="elm_checkbox_116_72_7048"]']

    locator_quick_filters_brand_button = ["xpath", '//div[@class="spoiler__title" and contains(text(), "Бренд")]']
    locator_quick_filters_brand_visible_checkbox = ["xpath", '(//div[@class="filters-checkbox__info" and '
                                                    'contains(text(), "Stool Group")])[2]']
    locator_quick_filters_brand_checkbox_stool_group = ["xpath", '//input[@id="elm_checkbox_116_21_275"]']

    locator_quick_filters_color_button = ["xpath", '//div[@class="spoiler__title" and contains(text(), "Цвет")]']
    locator_quick_filters_color_visible_checkbox = ["xpath", '(//div[@class="filters-checkbox__info" and '
                                                             'contains(text(), "орех")])[2]']
    locator_quick_filters_color_checkbox_walnut = ["xpath", '//input[@id="elm_checkbox_116_81_14283"]']

    locator_quick_filters_elements = ["xpath", '//div[@id="spoilerContainer"]']

    # Getters

    def get_value_quick_filters_price_range_min(self):
        return self.get_value_attribute(self.locator_quick_filters_price_range_min_input, 'value')

    def get_value_quick_filters_price_range_max(self):
        return self.get_value_attribute(self.locator_quick_filters_price_range_max_input, 'value')

    # Actions

    def click_quick_filters_price_range_button(self):
        self.click_visibility_element(self.locator_quick_filters_price_range)
        print("___Click Button 'Диапазон цены'")

    def click_quick_filters_in_stock_button(self):
        value = self.check_and_click_dropdown_is_displayed(self.locator_quick_filters_in_stock_button,
                                                           self.locator_quick_filters_in_stock_visible_checkbox)
        print("___Click Dropdown 'В наличии'. Status before click: " + str(
            value[0]) + "." + " Status after click: " + str(value[1]) + "." + " Check PASSED")

    def click_quick_filters_in_stock_checkbox(self):
        value = self.check_and_click_checkbox(self.locator_quick_filters_in_stock_checkbox, 'checked', 'true')
        print("___Click Checkbox 'В наличии'. Status before click: " + value[0] + "." + " Status after click: " +
              value[1] + "." + " Check PASSED")

    def click_quick_filters_category_button(self):
        value = self.check_and_click_dropdown_is_displayed(self.locator_quick_filters_category_button,
                                                           self.locator_quick_filters_category_visible_checkbox)
        print("___Click Dropdown 'Категория'. Status before click: " + str(
            value[0]) + "." + " Status after click: " + str(value[1]) + "." + " Check PASSED")

    def click_quick_filters_category_checkbox_tables(self):
        value = self.check_and_click_checkbox(self.locator_quick_filters_category_checkbox_tables, 'checked', 'true')
        print("___Click Checkbox 'Столы'. Status before click: " + value[0] + "." + " Status after click: " +
              value[1] + "." + " Check PASSED")

    def click_quick_filters_brand_button(self):
        value = self.check_and_click_dropdown_is_displayed(self.locator_quick_filters_brand_button,
                                                           self.locator_quick_filters_brand_visible_checkbox)
        print("___Click Dropdown 'Бренд'. Status before click: " + str(value[0]) + "." + " Status after click: " +
              str(value[1]) + "." + " Check PASSED")

    def click_quick_filters_brand_checkbox_stool_group(self):
        value = self.check_and_click_checkbox(self.locator_quick_filters_brand_checkbox_stool_group, 'checked', 'true')
        print(
            "___Click Checkbox 'Stool Group'. Status before click: " + value[0] + "." + " Status after click: " +
            value[1] + "." + " Check PASSED")

    def click_quick_filters_color_button(self):
        value = self.check_and_click_dropdown_is_displayed(self.locator_quick_filters_color_button,
                                                           self.locator_quick_filters_color_visible_checkbox)
        print("___Click Dropdown 'Цвет'. Status before click: " + str(value[0]) + "." + " Status after click: " +
              str(value[1]) + "." + " Check PASSED")

    def click_quick_filters_color_checkbox_walnut(self):
        value = self.check_and_click_checkbox(self.locator_quick_filters_color_checkbox_walnut, 'checked', 'true')
        print("___Click Checkbox 'Орех'. Status before click: " + value[0] + "." + " Status after click: " +
              value[1] + "." + " Check PASSED")

    # Methods

    def select_price_tables_scroll(self):

        """  Выбор мин. и макс. цены с помощью ползунка.
        Проверка на изменение мин. и макс. цены после взаимодействия с ползунком. """

        self.click_quick_filters_price_range_button()
        min_price_before = self.get_value_quick_filters_price_range_min()
        self.scroll_and_release(self.locator_quick_filters_price_range_min_scroll,
                                self.step_scroll_filter_price_rang_min)
        min_price_after = self.get_value_quick_filters_price_range_min()

        assert int(min_price_before) < int(min_price_after)
        print('___Select min price ' + str(min_price_after) + ' Min price before = ' + str(min_price_before) +
              'Check PASSED')

        self.click_quick_filters_price_range_button()
        max_price_before = self.get_value_quick_filters_price_range_max()
        self.scroll_and_release(self.locator_quick_filters_price_range_max_scroll,
                                self.step_scroll_filter_price_rang_max)
        max_price_after = self.get_value_quick_filters_price_range_max()

        assert int(max_price_before) > int(max_price_after)
        print("___Select max price " + str(min_price_after) + " Max price before = " + str(max_price_before) +
              " Check PASSED")

    def select_quick_filters_in_stock(self):

        """  Выбор чек-бокса - В наличии, в выпадающем списке - В наличии. """

        self.click_quick_filters_in_stock_button()
        self.click_quick_filters_in_stock_checkbox()

    def select_quick_filters_category_tables(self):

        """  Выбор чек-бокса - Стулья, в выпадающем списке - Категория. """

        self.click_quick_filters_category_button()
        self.click_quick_filters_category_checkbox_tables()

    def select_quick_filters_brand_stool_group(self):

        """  Выбор чек-бокса - Stool Group, в выпадающем списке - Бренд. """

        self.click_quick_filters_brand_button()
        self.click_quick_filters_brand_checkbox_stool_group()

    def select_quick_filters_color_walnut(self):

        """  Выбор чек-бокса - Орех, в выпадающем списке - Цвет. """

        self.click_quick_filters_color_button()
        self.click_quick_filters_color_checkbox_walnut()

    def check_availability_content(self):

        """  Проверка наличия всех параметров в быстром фильтре. """

        elements = self.get_text(self.locator_quick_filters_elements)
        for f in self.availability_content_quick_filters:
            assert f in elements
        print('___Check availability content. PASSED')
