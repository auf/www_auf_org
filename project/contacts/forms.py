from django import forms
from .models import Contacte
from auf.django.references.models import Region


class ContacteForm(forms.Form):
    sujet = forms.CharField(max_length=30)
    email = forms.EmailField()
    bureau = forms.ModelChoiceField(queryset=Region.objects.all())
    message = forms.CharField(widget=forms.Textarea)

