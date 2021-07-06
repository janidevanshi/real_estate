from django import forms
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
