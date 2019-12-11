# Generated by Django 2.2.6 on 2019-12-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название модели')),
                ('email', models.EmailField(blank=True, max_length=120, null=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон номера')),
                ('description', models.CharField(blank=True, max_length=120, null=True, verbose_name='Описание')),
                ('call_time', models.CharField(blank=True, max_length=120, null=True, verbose_name='Время звонка')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Формы обратной связи',
            },
        ),
    ]