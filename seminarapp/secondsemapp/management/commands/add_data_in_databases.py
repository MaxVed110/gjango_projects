from django.core.management.base import BaseCommand
from seminarapp.secondsemapp.models import Customer, Product, Cell


class Command(BaseCommand):
    help = 'add data in all databases'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count models')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            customer = Customer(name='aaa', email='ddd@dddd.rt', number_phone=862114555, address=223,
                                date_reg='10.1.1999')
            customer.save()
            product = Product(name_prod='sddf', description='wrrrr', price=556, count_prod=788, date_added='01.01.2000')
            product.save()
            cell = Cell(customer=customer, products=product, total_cost=55555, date_registration='02.02.2021')
            cell.save()

