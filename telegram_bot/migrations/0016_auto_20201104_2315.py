# Generated by Django 3.1.2 on 2020-11-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0014_auto_20201104_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draw',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Названия розыгрыша'),
        ),
    ]
