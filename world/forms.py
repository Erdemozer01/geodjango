from django.contrib.gis import forms
from .models import Zipcode, WorldBorder
from leaflet.forms.widgets import LeafletWidget


class ZipcodeForm(forms.ModelForm):
    class Meta:
        model = Zipcode
        fields = "__all__"
        widgets = {
            'point': LeafletWidget()
        }


class HomeWorldForm(forms.Form):
    point = forms.GeometryField(widget=LeafletWidget(attrs={'class': 'form-row field-mpoly'}), label="")
