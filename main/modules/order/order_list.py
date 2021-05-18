from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from main.models_addon.ya_market import Order, Item
from main.view import get_navbar, Page, Filtration
from main.ya_requests import OrderList
from main.modules.base import BaseView


class OrderListView(BaseView):
    """отображение каталога"""
    context = {'title': 'Order', 'page_name': 'Заказы'}
    models_to_save = [OrderList]
    fields = ['status', 'order_id', 'paymentType', 'total_price']
    filtration = Filtration({
        'status': 'Статус',
        'paymentType': 'Тип оплаты'
    })

    def post(self, request) -> HttpResponse:
        return self.save_models(request=request,  name='catalogue_order')

    def get(self, request) -> HttpResponse:
        orders = Order.objects.prefetch_related('items').filter(user=request.user)
        filter_types = self.filtration.get_filter_types(orders)
        local_context = {
            'navbar': get_navbar(request),
            'orders': self.sort_object(orders, filter_types),
            'table': ["Номер заказа", "Дата заказа", "Цена, ₽", "Статус"],
            'filter_types': filter_types.items(),
        }
        self.context_update(local_context)
        return render(request, Page.order, self.context)


class OrderPageView(BaseView):
    context = {'title': 'Order', 'page_name': 'Информация о заказе'}

    def get(self, request, pk) -> HttpResponse:
        item_id = int(request.GET.get('item_id', 0))
        if item_id:
            item = Item.objects.get(pk=item_id)
            offer_id = item.get_offer_id(self.request.user)
            if offer_id:
                return redirect(reverse('offer_by_sku', args=[offer_id]))
        order = get_object_or_404(Order, pk=pk)
        self.context_update({'navbar': get_navbar(request), 'order': order})
        return render(request, Page.order_page, self.context)
