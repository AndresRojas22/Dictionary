from django import forms

class wordForm(forms.Form):
    word = forms.CharField(label="word", max_length=100)