from django import forms
from CarsApp.models import Voiture

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['matricule', 'prix_jour', 'image', 'marque', 'model', 'disponibilite', 'categorie', 'carburant', 'description']
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Matricule'}),
            'prix_jour': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Daily Price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form__input', 'placeholder': 'Image'}),
            'marque': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Brand'}),
            'model': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Model'}),
            'disponibilite': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'categorie': forms.Select(attrs={'class': 'form-select form__input', 'placeholder': 'Category'}),
            'carburant': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Fuel Type'}),
            'description': forms.Textarea(attrs={'class': 'form__input', 'placeholder': 'Description'}),
   }
# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
# from CarsApp.models import Voiture

# class VoitureForm(forms.ModelForm):
#     class Meta:
#         model = Voiture
#         fields = ['matricule', 'prix_jour', 'image', 'marque', 'model', 'disponibilite', 'categorie', 'carburant', 'description']

#     def __init__(self, *args, **kwargs):
#         super(VoitureForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save'))
