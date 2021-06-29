from django.db import models
from django.db.models.aggregates import Max
from multiselectfield import MultiSelectField


MY_CHOICES = (('key1', 'Near to School'),
              ('key2', 'Near to Hospital'),
              ('key3', 'Close to Airport'),
              ('key4', 'Close to Market'))
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=250)
    subject = models.TextField()

    def __str__(self):
        return self.name


SELL_OR_RENT_CHOICES = (
    ('Sell', ('Sell')),
    ('Rent', ('Rent')),
)
PROPERTY_CHOICES = (
    ('Office', 'Office'),
    ('Shop', 'Shop'),
    ('Storage', 'Storage'),
    ('Land', 'Land'),
    ('Hospitality', 'Hospitality'),
    ('Other', 'Other')
)
STATUS_CHOICES = (
    ("Ready to Move", "Ready to Move"),
    ("Under Construction", "Under Construction"),
)


class Commercial(models.Model):
    main_image = models.ImageField(upload_to='images', default='none')
    Area = models.DecimalField(max_digits=5, decimal_places=2)
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    slug = models.CharField(max_length=100)
    sell_or_rent = models.CharField(max_length=20,
                                    choices=SELL_OR_RENT_CHOICES, blank=False)
    timestamp = models.DateTimeField(True)
    location = models.CharField(max_length=150)
    property_type = models.CharField(max_length=20,
                                     choices=PROPERTY_CHOICES, blank=False)
    floorplan = models.FileField(blank=True)
    construction_status = models.CharField(max_length=20,
                                           choices=STATUS_CHOICES, blank=False)
    amenities = MultiSelectField(choices=MY_CHOICES)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Commercial, default=None,
                             on_delete=models.CASCADE)
    images = models.FileField(upload_to='page_nav/images/')

    def __str__(self):
        return self.post.title
