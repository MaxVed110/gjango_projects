from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cell/<int:customer_id>/<int:period>', views.products, name='products')
]
