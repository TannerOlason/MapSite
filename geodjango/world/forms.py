from django.contrib.gis import forms
from django.contrib.gis.db.models import PointField
from . import models

class ThingForm(forms.ModelForm):
    geom = forms.PointField(widget= forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}) )
    class Meta:
        model = models.Things
        fields = ['title','description','geom',]
#test
#change
