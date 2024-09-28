from django import forms


class AddItemsForm(forms.Form):
    item = forms.CharField()
    quantity = forms.IntegerField()
