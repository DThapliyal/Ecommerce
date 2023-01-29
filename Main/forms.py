from django import forms
from .models import Ecommerce #import your Models from the models folder of your ProjectApp.


class addproduct(forms.ModelForm):
    class Meta:#we have used Meta to change the behaviour of our Model.
        model=Ecommerce
        fields=['name','categeory','price','details','image']#arrange the in a Order, you want to display on Screen.
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'categeory':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'details':forms.Textarea(attrs={'class':'form-control'}),
        }#widgets for adding the CSS.