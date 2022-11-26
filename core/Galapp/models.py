from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import qrcode
from PIL import Image
from django.contrib.auth.models import User


class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to='photo')
    thumbnail_path = models.ImageField(upload_to='thumbnails')
    title = models.CharField(verbose_name='Подпись', max_length=100)
    delete_flag = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Изображения"

    def __str__(self):
        return str(f"{self.user.username}")

    def save(self, *args, **kwargs):
        super(Gallery, self).save(*args, **kwargs)
        image = Image.open(self.image_path.path)
        width = image.width
        height = image.height
        if image.width > 640:
            width = 640
        if image.height > 480:
            height = 480
        output_size = (width, height)
        image.thumbnail(output_size)
        image.save(self.thumbnail_path.path)

    def delete(self, *args, **kwargs):
        storage, path = self.image_path.storage, self.image_path.path
        storage.delete(path)
        storage, path = self.thumbnail_path.storage, self.thumbnail_path.path
        super(Gallery, self).delete(*args, **kwargs)
        storage.delete(path)
