# Generated by Django 2.2.6 on 2019-11-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='price',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Цена'),
        ),
    ]