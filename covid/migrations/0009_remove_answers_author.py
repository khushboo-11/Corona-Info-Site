# Generated by Django 3.1.2 on 2020-11-17 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0008_auto_20201118_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='author',
        ),
    ]
