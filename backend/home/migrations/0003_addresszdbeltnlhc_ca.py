# Generated by Django 2.2.28 on 2022-11-18 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addresszdbeltnlhc'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresszdbeltnlhc',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]