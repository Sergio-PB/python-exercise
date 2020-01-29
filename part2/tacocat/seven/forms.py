from django import forms

class IntListForm(forms.Form):
    int_list = forms.CharField(label='Integers list')