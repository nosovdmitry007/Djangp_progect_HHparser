# Generated by Django 4.0.4 on 2022-05-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]
