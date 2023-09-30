from base.base_class import Base


class Main_page(Base):

    def __init__(self):
        super().__init__()

    # Test data

    url = 'https://stoolgroup.ru'

    # Locators

    locator_tables_button = ['xpath', '//a[@data-title="Столы"]']
    locator_tables_title = ['xpath', '//h1[@class="tp_h-2 mb-0" and contains(text(), "Столы")]']

    # Actions

    def click_and_check_tables_button(self):

        """ Нажатие на кнопку Столы, переход на страницу Столы, проверка страницы по ключевому слову. """

        self.click_clickable_element(self.locator_tables_button)
        value_title = self.asser_word(self.locator_tables_title, "Столы")
        print("___Click Button 'Столы'. Page title after clicking: " + value_title + " PASSED")
