# Generated by Django 5.0.4 on 2024-04-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='book/images'),
        ),
    ]
