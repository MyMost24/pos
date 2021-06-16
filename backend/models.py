from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return '{}'.format(self.name)


class HeatLevel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=255)
    img = models.FileField(upload_to='images/', null=True, blank=True, verbose_name="Image")
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    heat = models.ForeignKey(HeatLevel, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return  '{},{}'.format(self.product.name, self.heat.name)


class OrderDetail(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    type = models.ManyToManyField(ProductType, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class SweetLevel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)


class Member(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return '{},{}'.format(self.name, self.phone)

class Order(models.Model):
    product = models.ForeignKey(ProductPrice, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    count = models.IntegerField()
    voucher = models.IntegerField(default=0)
    detail = models.ManyToManyField(OrderDetail, null=True, blank=True)
    sweetlevel = models.ForeignKey(SweetLevel, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)


class SessionStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)


DEFAULT_MEMBER_ID = 1
class Session(models.Model):
    order = models.ManyToManyField(Order, blank=True, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, default=DEFAULT_MEMBER_ID)
    status = models.ForeignKey(SessionStatus, on_delete=models.CASCADE)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    close_at = models.DateTimeField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

