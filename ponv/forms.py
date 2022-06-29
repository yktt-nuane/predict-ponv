from django import forms


class ModelForm(forms.Form):
    height = forms.IntegerField(label='height')
    smoke = forms.IntegerField(label='smoke')
    anxiety = forms.IntegerField(label='anxiety')
