# Generated by Django 3.1.2 on 2020-11-17 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0006_auto_20201117_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='question',
            new_name='ques',
        ),
    ]
