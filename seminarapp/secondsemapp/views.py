from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from .models import Customer, Product, Cell
from .forms import EditDataProduct, SaveImg
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


def edit_prod(request):
    if request.method == 'POST':
        form = EditDataProduct(request.POST)
        if form.is_valid():
            id_prod = form.cleaned_data['id_prod']
            name_prod = form.cleaned_data['name_prod']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count_prod = form.cleaned_data['count_prod']
            date_added = form.cleaned_data['date_added']
            prod = Product.objects.filter(id=id_prod).first
            prod.name_prod = name_prod
            prod.description = description
            prod.price = price
            prod.count_prod = count_prod
            prod.date_added = date_added
            prod.save()
    else:
        form = EditDataProduct()
    return render(request, 'secondsemapp/upload_image.html', {'form': form})


def upload_img(request):
    if request.method == 'POST':
        form = SaveImg(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = SaveImg()
    return render(request, 'secondsemapp/upload_image.html', {'form': form})
