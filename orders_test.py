import data
import zakas
import json
# Ласточкина Анжелика, 13-я когорта, Марс — Финальный проект. Инженер по тестированию плюс
def test_success_order():
    new_order = zakas.post_new_order(data.GREAT_ORDER)
    assert new_order.status_code == 201
    new_order_json = new_order.json()

    print(new_order.status_code)
    print(new_order_json["track"])

    return new_order_json["track"]


def test_get_order_body_code():
    track_n = test_success_order() # Получаем track_n из другой функции
    order_body = zakas.get_new_order(track=track_n).status_code  # Используем track_n здесь
    assert order_body == 200
    print(order_body)


def test_get_order_body_po_number():
    track_n = test_success_order()  # Получаем track_n из другой функции
    order_body_number = zakas.get_new_order(track=track_n).text
    order_body_number_dict = json.loads(order_body_number)  # Преобразование строки в словарь
    print(order_body_number_dict)

    assert order_body_number_dict["order"]["track"] == track_n
