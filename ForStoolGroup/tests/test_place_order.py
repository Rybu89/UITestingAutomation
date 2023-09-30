from pages.checkout_page import Checkout_page

ChP = Checkout_page()


def test_order_selfdelivery_privateperson_onlinepay(from_test_place_orders):
    """ Оформление заказа с параметрами:
        - заполнение раздела контактная информация;
        - самовывоз;
        - физ. лицо;
        - использование промокода. """

    ChP.add_contact_information()
    ChP.select_self_delivery_method()
    ChP.select_private_person_entity()
    ChP.select_online_payment()
    ChP.select_promo_code()
    ChP.click_apply_button()

def test_availability_of_parameters(from_test_place_orders):
    """ Проверка на наличие параметров на странице:
        - Контактная информация (имя, фамилия, телефон, e-mail);
        - Адрес доставки
        - Способ доставки (самовывоз по адресу; доставка в пределах МКАД);
        - Физическое лицо (онлайн оплата, оплатить при получении);
        - Использовать бонусы или промокод (промокод, бонусы);
        - Подтверждение (товар, артикул, цена за шт., количество, общая цена, сумма);
        - Комментарий к заказу (текст - "Есть вопросы или уточнения? Введите сообщение");
        - согласие на обработку персональных данных;
        - подтверждение заказа (кнопка - "Оформить заказ", текст - "или", кнопка - "Сплит - оплата частями",
            кнопка - "Оплата с Я-Пей"). """

    ChP.check_presence_of_parameter_contact_information()
    ChP.check_presence_of_parameter_delivery_address()
    ChP.check_presence_of_parameter_delivery_method()
    ChP.check_presence_of_parameter_private_person()
    ChP.check_presence_of_promocode()
    ChP.check_presence_of_confirmation()
    ChP.check_presence_of_comment()
