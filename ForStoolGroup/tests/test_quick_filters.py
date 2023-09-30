from pages.quick_filters_for_furniture import Quick_filters_for_furniture

Qff = Quick_filters_for_furniture()


def test_quick_filters(from_test_quick_filters):

    """    Проверка, быстрого фильтра на странице "Столы". """

    Qff.check_availability_content()
    Qff.select_price_tables_scroll()
    Qff.select_quick_filters_in_stock()
    Qff.select_quick_filters_category_tables()
    Qff.select_quick_filters_brand_stool_group()
    Qff.select_quick_filters_color_walnut()
