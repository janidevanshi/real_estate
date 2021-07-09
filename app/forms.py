from django import forms
from django.db.models import fields
from .models import *


class CommercialForm(forms.ModelForm):
    class Meta:
        model = Commercial
        fields = "__all__"


class ImageForm(forms.ModelForm):
    images = forms.ImageField(label='Image')

    class Meta:
        model = PostImage
        fields = ('images', )


class ResidentialForm(forms.ModelForm):
    class Meta:
        model = Residential
        fields = "__all__"


class ResiImageForm(forms.ModelForm):
    images = forms.ImageField(label='Image')

    class Meta:
        model = PostRESIImage
        fields = ('images', )
