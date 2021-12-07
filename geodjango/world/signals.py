#credit: https://stackoverflow.com/questions/62739178/django-save-multiple-versions-of-an-image

import io
import sys

from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete

from .models import PanoImg

#  DRY
def image_resized(image, h):
    name = image.name
    _image = Image.open(image)
    content_type = Image.MIME[_image.format]
    r = h / _image.size[1]  # ratio
    w = int(_image.size[0] * r)
    imageTemproaryResized = _image.resize((w, h))
    file = io.BytesIO()
    imageTemproaryResized.save(file, _image.format)
    file.seek(0)
    size = sys.getsizeof(file)
    return file, name, content_type, size


@receiver(pre_save, sender=PanoImg, dispatch_uid='panoimg.save_image')
def save_image(sender, instance, **kwargs):
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    # add image (picture | thumbnail)
    if instance._state.adding:

        #  picture
        file, name, content_type, size = image_resized(instance.picture, 500)
        instance.picture = InMemoryUploadedFile(file, 'ImageField', name, content_type, size, None)

        #  picture_tn
        file, name, content_type, size = image_resized(instance.picture, 50)
        instance.picture_tn = InMemoryUploadedFile(file, 'ImageField', name, content_type, size, None)


    # update image (picture | thumbnail)
    if not instance._state.adding:
        # we have 2 cases:
        # - replace old with new
        # - delete old (when 'clear' checkbox is checked)

        #  picture
        old = sender.objects.get(pk=instance.pk).picture
        new = instance.picture
        if (old and not new) or (old and new and old.url != new.url):
            old.delete(save=False)

        #  picture_tn
        old = sender.objects.get(pk=instance.pk).picture_tn
        new = instance.picture_tn
        if (old and not new) or (old and new and old.url != new.url):
            old.delete(save=False)


@receiver(pre_delete, sender=PanoImg, dispatch_uid='panoimg.delete_image')
def delete_image(sender, instance, **kwargs):
    s = sender.objects.get(pk=instance.pk)

    if (not s.picture or s.picture is not None) and (not s.picture_tn or s.picture_tn is not None):
        s.picture.delete(False)
        s.picture_tn.delete(False)
