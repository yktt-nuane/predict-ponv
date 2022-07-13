from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class ModelForm(forms.Form):
    age = forms.IntegerField(label='age',validators=[MinValueValidator(20), MaxValueValidator(120)], help_text='')
    sex = forms.IntegerField(label='sex',validators=[MinValueValidator(0), MaxValueValidator(1)], help_text='Female enter 0, Male enter 1.')
    smoke = forms.IntegerField(label='smoke',validators=[MinValueValidator(0), MaxValueValidator(1)], help_text='if you never smoked enter 0, else enter 1.')
    ponv_history = forms.IntegerField(label='ponv_history',validators=[MinValueValidator(0), MaxValueValidator(1)], help_text='If you have experienced PONV or motion sickness enter 0, others enter 1.')
    anxiety = forms.IntegerField(label='anxiety',validators=[MinValueValidator(0), MaxValueValidator(21)], help_text='Enter the degree of anxiety as a number from 0 to 21.')


