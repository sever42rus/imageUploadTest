import os
from PIL import Image as PILImage
from io import BytesIO

from django.db import models
from django.core.files.base import ContentFile


class Image(models.Model):
    img = models.ImageField(upload_to='images', verbose_name='Изображение',)

    def save(self, *args, **kwargs):
        if not self.make_thumb():
            raise Exception(
                'Could not create thumbnail - is the file type valid?')
        super().save(*args, **kwargs)

    def make_thumb(self):

        image = PILImage.open(self.img)
        image.thumbnail((1280, 720), PILImage.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.img.name)
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False

        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        self.img.save(thumb_filename, ContentFile(
            temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

    class Meta:
        verbose_name_plural = "Изображения"
        verbose_name = "Изображение"
