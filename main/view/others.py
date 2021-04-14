import json
from django.shortcuts import render
from pygments import highlight, lexers, formatters

from main.models.save_dir import OfferPattern, OrderPattern, PricePattern
from main.yandex import OrderList


def get_json_data_from_file(file):
    """
    Загрузка данных из файла file
    """
    with open(file, "r", encoding="utf-8") as read_file:
        json_object = json.load(read_file)
    return json_object


def orders_list(request):
    json_object = get_json_data_from_file("orders_file.json")

    formatted_json = json.dumps(json_object, indent=2, ensure_ascii=False)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.HtmlFormatter())
    context = {
        'highlight_style': formatters.HtmlFormatter().get_style_defs('.highlight'),
        'content': colorful_json,
    }

    # OrderPattern(json=json_object['result']['orders']).save()  # из файла
    OrderList().save()  # из Яндекса

    return render(request, 'orders.html', context)


def save_db_from_files(request):
    """Восстановление бд из файлов"""
    json_object_offer = get_json_data_from_file("offer_data.json")
    OfferPattern(json=json_object_offer['result']['offerMappingEntries']).save(request.user)
    json_object_order = get_json_data_from_file("order_data.json")
    OrderPattern(json=json_object_order['result']['orders']).save(request.user)
    json_object_prise = get_json_data_from_file("price_data.json")
    PricePattern(json=json_object_prise['result']['offers']).save(request.user)

    return render(request, 'save_db.html')
