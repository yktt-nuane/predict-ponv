from django import forms


class ModelForm(forms.Form):
    age = forms.IntegerField(label='age')
    height = forms.IntegerField(label='height')
    weight = forms.IntegerField(label='weight')
    anxiety = forms.IntegerField(label='anxiety')
