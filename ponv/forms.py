from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class ModelForm(forms.Form):
    age = forms.IntegerField(label='age',validators=[MinValueValidator(20), MaxValueValidator(120)], help_text='')
    gender = forms.IntegerField(label='gender',validators=[MinValueValidator(0), MaxValueValidator(1)], help_text='Male enter 0, Female enter 1.')
    smoking_history = forms.IntegerField(label='smoking history',validators=[MinValueValidator(0), MaxValueValidator(1)], help_text='if you never smoking_historyd enter 0, else enter 1.')
    history_of_PONV = forms.IntegerField(label='history of PONV',validators=[MinValueValidator(0), MaxValueValidator(1)], help_text='If you have experienced PONV enter 0, others enter 1.')
    anxiety = forms.IntegerField(label='anxiety score',validators=[MinValueValidator(0), MaxValueValidator(21)], help_text='Enter the anxiety score from 0 to 21.')


