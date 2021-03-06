# Generated by Django 3.1.2 on 2020-11-17 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0005_auto_20201117_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='answers',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='questions',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_question', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(help_text='Your question!', max_length=2048),
        ),
    ]
