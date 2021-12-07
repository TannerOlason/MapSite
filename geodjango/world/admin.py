import os
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Entry, Things, PanoImg
from django.conf import settings
from django.utils.safestring import mark_safe

def get_panoimg_cover(obj):
    src = obj.picture.url if obj.picture and \
    hasattr(obj.picture, 'url') else os.path.join(
        settings.STATIC_URL, 'images/default.jpg')
    return mark_safe('<img src="{}" height="500" style="border:1px solid #ccc">'.format(src))
get_panoimg_cover.short_description = ''
get_panoimg_cover.allow_tags = True

def get_panoimg_cover_thumbnail(obj):
    src = obj.picture_tn.url if obj.picture_tn and \
    hasattr(obj.picture_tn, 'url') else os.path.join(
        settings.STATIC_URL, 'images/default_thumbnail.jpg')
    return mark_safe('<img src="{}" height="175" style="border:1px solid #ccc">'.format(src))
get_panoimg_cover_thumbnail.short_description = ''
get_panoimg_cover_thumbnail.allow_tags = True

@admin.register(Entry)
class EntryAdmin(OSMGeoAdmin):
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 12

@admin.register(Things)
class EntryAdmin(OSMGeoAdmin):
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 12
    display_wkt = True

@admin.register(PanoImg)
class EntryAdmin(OSMGeoAdmin):
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 1
    display_wkt = True
    fields = (
        'title', 'description', 'geom',
        get_panoimg_cover, get_panoimg_cover_thumbnail, 'picture',
    )
    readonly_fields = (get_panoimg_cover, get_panoimg_cover_thumbnail)
    
