# Generated by Django 5.0 on 2024-04-09 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0002_rename_addressdetails_vendordtails_address_details_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registermodel',
        ),
    ]
