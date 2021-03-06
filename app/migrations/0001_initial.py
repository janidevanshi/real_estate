# Generated by Django 3.2.3 on 2021-07-07 06:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('main_image', models.ImageField(default='none', upload_to='images/')),
                ('Area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('price', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('sell_or_rent', models.CharField(choices=[('Sell', 'Sell'), ('Rent', 'Rent')], max_length=20)),
                ('location', models.CharField(max_length=150)),
                ('property_type', models.CharField(choices=[('Office', 'Office'), ('Shop', 'Shop'), ('Storage', 'Storage'), ('Land', 'Land'), ('Hospitality', 'Hospitality'), ('Other', 'Other')], max_length=20)),
                ('floorplan', models.ImageField(blank=True, upload_to='')),
                ('construction_status', models.CharField(choices=[('Ready to Move', 'Ready to Move'), ('Under Construction', 'Under Construction')], max_length=20)),
                ('amenities', multiselectfield.db.fields.MultiSelectField(choices=[('key1', 'Near to School'), ('key2', 'Near to Hospital'), ('key3', 'Close to Airport'), ('key4', 'Close to Market')], max_length=19)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=250)),
                ('subject', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Residential',
            fields=[
                ('main_image', models.ImageField(default='none', upload_to='images')),
                ('Area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('price', models.IntegerField()),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('sell_or_rent', models.CharField(choices=[('Sell', 'Sell'), ('Rent', 'Rent')], max_length=20)),
                ('timestamp', models.DateTimeField(verbose_name=True)),
                ('location', models.CharField(max_length=150)),
                ('property_type', models.CharField(choices=[('RK', 'RK'), ('1 BHK', '1 BHK'), ('1.5 BHK', '1.5 BHK'), ('2 BHK', '2 BHK'), ('2.5 BHK', '2.5 BHK'), ('3 BHK', '3 BHK'), ('3.5 BHK', '3.5 BHK'), ('4 BHK', '4 BHK'), ('5 BHK', '5 BHK')], max_length=20)),
                ('floorplan', models.FileField(blank=True, upload_to='')),
                ('construction_status', models.CharField(choices=[('Ready to Move', 'Ready to Move'), ('Under Construction', 'Under Construction')], max_length=20)),
                ('amenities', multiselectfield.db.fields.MultiSelectField(choices=[('key1', 'Near to School'), ('key2', 'Near to Hospital'), ('key3', 'Close to Airport'), ('key4', 'Close to Market'), ('key5', 'Swimming Pool'), ('key6', 'Gym/Fitness Centers'), ('key7', 'Community Clubhouse'), ('key8', 'Community Garden'), ('key9', 'Guest Parking'), ('key10', 'Security Guards'), ('key11', 'CCTV Camera Security'), ('key12', 'Power Backup'), ('key13', '24/7 Water supply'), ('key14', 'Movie Theater'), ('key15', 'Waste disposal'), ('key16', 'Fire Fighting Systems'), ('key17', 'Senior Citizen Sitout'), ('key18', 'Vastu Compliant'), ('key19', 'Entrance Lobby')], max_length=104)),
            ],
        ),
        migrations.CreateModel(
            name='PostRESIImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='resipage_nav/images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.residential')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.commercial')),
            ],
        ),
    ]
