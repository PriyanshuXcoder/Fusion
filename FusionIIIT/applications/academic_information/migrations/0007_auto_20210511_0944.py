# Generated by Django 3.1.5 on 2021-05-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0006_auto_20210422_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hall_no',
            field=models.IntegerField(default=0),
        ),
    ]