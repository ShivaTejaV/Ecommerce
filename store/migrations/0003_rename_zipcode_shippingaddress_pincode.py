# Generated by Django 5.1.6 on 2025-03-11 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zipcode',
            new_name='pincode',
        ),
    ]
