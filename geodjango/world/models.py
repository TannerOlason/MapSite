from django.contrib.gis.db.models import PointField
from django.contrib.gis.db import models
from django.utils.translation import gettext as _

class Things(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    description = models.CharField(max_length=1000)
    geom = models.PointField()

    @property
    def lat_lng(self):
        return list(getattr(self.geom, 'coords', [])[::-1])

    def __unicode__(self):
        return self.title

class PanoImg(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)
    #picture = models.ImageField(upload_to='static/images/',max_length=1000)
    geom = models.PointField()

    def upload(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(filename.split('.')[0], ext)
        path = 'static/images/'
        return '{}{}'.format(path,filename)

    picture = models.ImageField('Pano Img',
        upload_to=upload,
        null=True, blank=True,
        help_text=_('Upload Pano Image')
    )

    def upload_thumb(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}_thumbnail.{}'.format(filename.split('.')[0], ext)
        path = 'static/images/'
        return '{}{}'.format(path, filename)

    picture_tn = models.ImageField('Pano Thumbnail',
        upload_to=upload_thumb,  # callback function
        null=True, blank=True,
        help_text=_('Upload Pano Image Thumbnail')
    )

    def save(self, *args, **kwargs):

        # i moved the logic to signals

        # if not self.slug:
            # self.slug = slugify(self.title)
        super(PanoImg, self).save(*args, **kwargs)

class Blog(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=200)

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    headline = models.CharField(max_length=255)
    point = PointField()
    @property
    def lat_lng(self):
        return list(getattr(self.point, 'coords', [])[::-1])
