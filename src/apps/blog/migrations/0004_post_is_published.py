# Generated by Django 4.2.4 on 2023-08-31 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовать'),
        ),
    ]