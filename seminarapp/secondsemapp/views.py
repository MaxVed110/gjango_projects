from django.shortcuts import render, get_object_or_404
from seminarapp.secondsemapp.models import Customer, Product, Cell
import datetime


def index(request):
    content = {'name': 'Главная'}
    return render(request, "secondsemapp/index.html", content)


def products(request, customer_id, period):
    period = 7 if period <= 7 else 30 if 7 < period <= 30 else 365
    customer = get_object_or_404(Customer, pk=customer_id)
    data = datetime.datetime.today() - datetime.timedelta(days=period)
    list_products = []
    while data <= datetime.datetime.today():
        list_products.append(
            Cell.objects.filter(customer=customer, date_registration=data).order_by('date_registration'))
        data = data + datetime.timedelta(days=1)

    list_products = [i.products for i in list_products]

    content = {'name': 'Заказы', 'period': period, 'list_products': list_products}
    return render(request, "secondsemapp/product.html", content)
