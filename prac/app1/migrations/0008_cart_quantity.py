# Generated by Django 3.2.8 on 2021-11-26 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20211125_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
