from django.urls import path
from django.views.generic import ListView
from djgeojson.views import GeoJSONLayerView
from .models import Things
from . import views

app_name = 'world'

context = {
    'current':'world'
}

urlpatterns = [
    path('add/', views.insert_thing, name="insert_thing"),
    path('map/', views.show_things, name="show_things"),
    path('',views.Home.as_view(), name="map"),
    path('things_data/', views.things_dataset, name='the_things'),
    path('pano_data/', views.pic_dataset, name='pano_imgs'),
    path('show/', views.show360, name = 'show'),
    path('basic/', views.show_basic, name="basic"),
]
