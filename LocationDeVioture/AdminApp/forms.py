from django import forms
from CarsApp.models import Voiture
import re #pour effectuer des opérations d'expressions régulières

class VoitureForm(forms.ModelForm): # formulaire basé sur un modèle Django existant
    class Meta:
        model = Voiture
        fields = ['matricule', 'prix_jour', 'marque', 'model', 'categorie', 'carburant', 'KM', 'State', 'Availability', 'description', 'image']

        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Matricule'}),
            'prix_jour': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Daily Price'}),
            'image': forms.FileInput(attrs={'class': 'form__input', 'placeholder': 'Image'}),
            'marque': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Brand'}),
            'model': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Model'}),
            'categorie': forms.Select(attrs={'class': 'form-select form__input', 'placeholder': 'Category'}),
            'carburant': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Fuel Type'}),
            'KM': forms.NumberInput(attrs={'class': 'form__input', 'placeholder': 'Kilometers'}),
            'State': forms.Select(attrs={'class': 'form-select form__input', 'placeholder': 'State'}),
            'Availability': forms.Select(attrs={'class': 'form-select form__input', 'placeholder': 'Availability'}),
            'description': forms.Textarea(attrs={'class': 'form__input', 'placeholder': 'Description'}),
        }

    def clean_matricule(self):
        matricule = self.cleaned_data.get('matricule')
        if not re.match(r'^\d{5}/[A-Z]/\d{2}$', matricule):
            raise forms.ValidationError('The matricule is not valid. Please use the correct format.')
        return matricule
