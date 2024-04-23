from django import forms
from author.models import *
class NewBookForm(forms.Form):
    title = forms.CharField(max_length=200,required=True)
    version = forms.IntegerField()
    image = forms.FileField(max_length=100)
    author=forms.ChoiceField(choices=Author.Get_all())