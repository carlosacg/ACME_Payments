# Generated by Django 3.1.4 on 2023-03-25 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='quantity_hours',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='total_price',
        ),
    ]