# Generated by Django 4.1 on 2022-11-26 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Galapp', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.ImageField(upload_to='photo')),
                ('thumbnail_path', models.ImageField(upload_to='thumbnails')),
                ('title', models.CharField(max_length=100, verbose_name='Подпись')),
                ('delete_flag', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Uploaded Images',
            },
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
