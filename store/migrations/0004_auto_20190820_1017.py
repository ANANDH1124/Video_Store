# Generated by Django 2.2.4 on 2019-08-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20190820_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='runtime',
            field=models.CharField(max_length=120),
        ),
    ]
