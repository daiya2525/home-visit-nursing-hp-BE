# Generated by Django 2.2.4 on 2022-01-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220114_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.CharField(max_length=10000),
        ),
    ]