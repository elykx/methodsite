# Generated by Django 4.0.5 on 2022-06-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('methods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrix',
            name='step',
            field=models.FloatField(default=0.1, verbose_name='Шаг'),
        ),
    ]