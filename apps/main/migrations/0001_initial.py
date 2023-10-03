# Generated by Django 4.2.5 on 2023-10-02 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='сообщение')),
                ('recipient', models.EmailField(max_length=200, verbose_name='почта получателя')),
                ('how_many_messages', models.IntegerField(default=1, verbose_name='сколько отправить сообщений')),
                ('interval', models.PositiveSmallIntegerField(choices=[(0, '1 минута'), (1, '5 минут'), (2, '10 минут'), (3, '15 минут'), (4, '30 минут'), (5, '45 минут'), (6, '1 час'), (7, '6 часов'), (8, '12 часов'), (9, '24 часа')], default=0, verbose_name='промежуток между сообщениями')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='кто отправил')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['-sender'],
            },
        ),
    ]
