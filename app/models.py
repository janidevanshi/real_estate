from django.db import models
from django.db.models.aggregates import Max

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=250)
    subject = models.TextField()

    def __str__(self):
        return self.name


SELL_OR_RENT_CHOICES = (
    (1, "Sell"),
    (2, "Rent"),
)


class Commercial(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    slug = models.CharField(max_length=100)
    sell_or_rent = models.IntegerField(
        choices=SELL_OR_RENT_CHOICES, blank=False)
    timestamp = models.DateTimeField(True)

    def __str__(self):
        return self.title
