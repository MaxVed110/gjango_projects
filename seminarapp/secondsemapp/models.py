from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    number_phone = models.CharField(max_length=20)
    address = models.TextField()
    date_reg = models.DateField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name_prod = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=1)
    count_prod = models.DecimalField(max_digits=10, decimal_places=0)
    date_added = models.DateField()
    product_img = models.ImageField(upload_to='products/', default=None)

    def __str__(self):
        return self.name_prod


class Cell(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_cost = models.DecimalField(max_digits=15, decimal_places=1)
    date_registration = models.DateField()

    def __str__(self):
        return self.customer
