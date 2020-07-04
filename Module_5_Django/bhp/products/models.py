from django.db import models

from django.conf import settings


USER_MODEL = settings.AUTH_USER_MODEL


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Purchase(TimeStampModel):
    user_id = models.ForeignKey(USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    make_refund_status = models.BooleanField(default=False)


class Refund(TimeStampModel):
    purchase_id = models.OneToOneField(Purchase, on_delete=models.CASCADE, blank=True, null=True)
    confirmation = models.BooleanField(blank=True, null=True)
