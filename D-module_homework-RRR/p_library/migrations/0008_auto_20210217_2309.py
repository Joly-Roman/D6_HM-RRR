# Generated by Django 2.2.6 on 2021-02-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20210217_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../media/book_photos/', verbose_name='Фото'),
        ),
    ]
