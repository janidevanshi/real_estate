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


class Commercial(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    timestamp = models.DateTimeField(True)

    def __str__(self):
        return self.title
