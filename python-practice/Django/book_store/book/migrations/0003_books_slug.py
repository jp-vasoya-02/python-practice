# Generated by Django 3.2.6 on 2021-10-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20211018_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
