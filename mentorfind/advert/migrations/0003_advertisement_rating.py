# Generated by Django 5.0.1 on 2024-03-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='rating',
            field=models.PositiveIntegerField(default=5),
        ),
    ]