from django import forms
from .models import FormsModel

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)

    def clean_name(self):
        print("I am from form", self.cleaned_data)
        name = self.cleaned_data['name']
        # I can do any validation or clean the name.
        return name.lower()

class FormsModelForm(forms.ModelForm):
    class Meta:
         model = FormsModel
         fields = ['name', 'email']