# Generated by Django 4.0.1 on 2022-01-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_book_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_link',
            field=models.URLField(default='https://cloudfront.penguin.co.in/wp-content/uploads/2022/01/9780143454441.jpg', max_length=1000),
        ),
    ]
