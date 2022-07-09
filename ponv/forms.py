from django import forms


class ModelForm(forms.Form):
    age = forms.IntegerField(label='age')
    sex = forms.IntegerField(label='sex')
    smoke = forms.IntegerField(label='smoke')
    ponv_history = forms.IntegerField(label='ponv_history')
    anxiety = forms.IntegerField(label='anxiety')
