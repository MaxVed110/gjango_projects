from django import forms


class EditDataProduct(forms.Form):
    id_prod = forms.IntegerField()
    name_prod = forms.CharField(max_length=100)
    description = forms.CharField()
    price = forms.DecimalField(max_digits=10, decimal_places=1)
    count_prod = forms.DecimalField(max_digits=10, decimal_places=0)
    date_added = forms.DateField()


class SaveImg(forms.Form):
    image = forms.ImageField()
