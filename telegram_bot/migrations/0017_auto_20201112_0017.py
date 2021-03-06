# Generated by Django 3.1.2 on 2020-11-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0016_auto_20201104_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_competition',
            field=models.CharField(choices=[('is_rebus', 'РЕБУС'), ('is_poll', 'ОПРОС'), ('is_registration', 'РЕГИСТРАЦИЯ')], default='is_registration', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='is_current_rebus_finished',
            field=models.BooleanField(default=False),
        ),
    ]
