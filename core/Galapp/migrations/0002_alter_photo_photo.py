# Generated by Django 4.1.2 on 2022-11-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Galapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/photo', verbose_name='Фотография'),
        ),
    ]