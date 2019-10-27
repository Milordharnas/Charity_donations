from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

INSTITUTION_TYPES = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s" % (self.name)


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default=None)
    types = models.IntegerField(choices=INSTITUTION_TYPES, default=1)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return "%s" % (self.name)


class Donation(models.Model):
    quantity = models.IntegerField()
    category = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=32)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
