from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class ModelForm(forms.Form):
    age = forms.IntegerField(label='age',validators=[MinValueValidator(20), MaxValueValidator(120)])
    sex = forms.IntegerField(label='sex',validators=[MinValueValidator(0), MaxValueValidator(1)])
    smoke = forms.IntegerField(label='smoke',validators=[MinValueValidator(0), MaxValueValidator(1)])
    ponv_history = forms.IntegerField(label='ponv_history',validators=[MinValueValidator(0), MaxValueValidator(1)])
    anxiety = forms.IntegerField(label='anxiety',validators=[MinValueValidator(0), MaxValueValidator(21)])
