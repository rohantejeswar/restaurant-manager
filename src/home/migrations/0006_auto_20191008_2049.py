# Generated by Django 2.2.5 on 2019-10-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191008_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
