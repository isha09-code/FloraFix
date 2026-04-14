# from django import forms

# class UploadImageForm(forms.Form):
#     image = forms.ImageField()
from django import forms

class UploadImageForm(forms.Form):
    plantImage = forms.ImageField()
