from django.db import models
from django.db.models.aggregates import Max
from multiselectfield import MultiSelectField
from django.utils.timezone import now
from django.template.defaultfilters import slugify

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=250)
    subject = models.TextField()

    def __str__(self):
        return self.name


MY_COMM_CHOICES = (('key1', 'Near to School'),
                   ('key2', 'Near to Hospital'),
                   ('key3', 'Close to Airport'),
                   ('key4', 'Close to Market'))

SELL_OR_RENT_COMM_CHOICES = (
    ('Sell', ('Sell')),
    ('Rent', ('Rent')),
)
COMM_PROPERTY_CHOICES = (
    ('Office', 'Office'),
    ('Shop', 'Shop'),
    ('Storage', 'Storage'),
    ('Land', 'Land'),
    ('Hospitality', 'Hospitality'),
    ('Other', 'Other')
)
COMM_STATUS_CHOICES = (
    ("Ready to Move", "Ready to Move"),
    ("Under Construction", "Under Construction"),
)


class Commercial(models.Model):
    main_image = models.ImageField(
        upload_to='images/', default='none')
    Area = models.DecimalField(max_digits=10, decimal_places=2)
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    # slug = models.SlugField(blank=False, unique=True)
    timestamp = models.DateTimeField(default=now)
    sell_or_rent = models.CharField(max_length=20,
                                    choices=SELL_OR_RENT_COMM_CHOICES)
    location = models.CharField(max_length=150)
    property_type = models.CharField(max_length=20,
                                     choices=COMM_PROPERTY_CHOICES)
    floorplan = models.ImageField(blank=True)
    construction_status = models.CharField(max_length=20,
                                           choices=COMM_STATUS_CHOICES)
    amenities = MultiSelectField(choices=MY_COMM_CHOICES)

    def __str__(self):
        return self.title + ('    ') + self.location


# def get_image_filename(instance, filename):
#     title = instance.post.title
#     slug = slugify(title)
#     return "commercial/%s-%s" % (slug, filename)


class PostImage(models.Model):
    post = models.ForeignKey(Commercial, default=None,
                             on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.post.title


MY_RESI_CHOICES = (('key1',  'Near to School'),
                   ('key2',  'Near to Hospital'),
                   ('key3',  'Close to Airport'),
                   ('key4',  'Close to Market'),
                   ('key5',  'Swimming Pool'),
                   ('key6',  'Gym/Fitness Centers'),
                   ('key7',  'Community Clubhouse'),
                   ('key8',  'Community Garden'),
                   ('key9',  'Guest Parking'),
                   ('key10',  'Security Guards'),
                   ('key11',  'CCTV Camera Security'),
                   ('key12',  'Power Backup'),
                   ('key13',  '24/7 Water supply'),
                   ('key14',  'Movie Theater'),
                   ('key15',  'Waste disposal'),
                   ('key16',  'Fire Fighting Systems'),
                   ('key17',  'Senior Citizen Sitout'),
                   ('key18',  'Vastu Compliant'),
                   ('key19',  'Entrance Lobby'))


SELL_OR_RENT_RESI_CHOICES = (
    ('Sell', ('Sell')),
    ('Rent', ('Rent')),
)
RESI_PROPERTY_CHOICES = (
    ('RK', 'RK'),
    ('1 BHK', '1 BHK'),
    ('1.5 BHK', '1.5 BHK'),
    ('2 BHK', '2 BHK'),
    ('2.5 BHK', '2.5 BHK'),
    ('3 BHK', '3 BHK'),
    ('3.5 BHK', '3.5 BHK'),
    ('4 BHK', '4 BHK'),
    ('5 BHK', '5 BHK'),
)

RESI_STATUS_CHOICES = (
    ("Ready to Move", "Ready to Move"),
    ("Under Construction", "Under Construction")
)


class Residential(models.Model):
    main_image = models.ImageField(
        upload_to='images', default='none', blank=False)
    Area = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    price = models.IntegerField(blank=False)
    slug = models.CharField(max_length=100, blank=False, unique=True)
    sell_or_rent = models.CharField(max_length=20,
                                    choices=SELL_OR_RENT_RESI_CHOICES, blank=False)
    timestamp = models.DateTimeField(True)
    location = models.CharField(max_length=150, blank=False)
    property_type = models.CharField(max_length=20,
                                     choices=RESI_PROPERTY_CHOICES, blank=False)
    floorplan = models.FileField(blank=True)
    construction_status = models.CharField(max_length=20,
                                           choices=RESI_STATUS_CHOICES, blank=False)
    amenities = MultiSelectField(choices=MY_RESI_CHOICES)

    def __str__(self):
        return self.title + ('    ') + self.location


class PostRESIImage(models.Model):
    post = models.ForeignKey(Residential, default=None,
                             on_delete=models.CASCADE)
    images = models.FileField(upload_to='resipage_nav/images/')

    def __str__(self):
        return self.post.title
