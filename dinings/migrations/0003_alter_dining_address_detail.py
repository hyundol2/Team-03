# Generated by Django 3.2.18 on 2023-04-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinings', '0002_dining_address_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dining',
            name='address_detail',
            field=models.CharField(max_length=20),
        ),
    ]
