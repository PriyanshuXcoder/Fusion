# Generated by Django 3.1.5 on 2024-11-16 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0005_merge_20241116_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]