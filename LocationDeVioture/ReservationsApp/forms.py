from django import forms

class ReservationForm(forms.Form):
    nom = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form__input','placeholder': 'Client Name'}))
    prenom = forms.CharField(label='Surname', max_length=100, widget=forms.TextInput(attrs={'class': 'form__input','placeholder': 'Client Surname'}))
    date_debut = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'class': 'form-select form__input','type': 'date', 'placeholder': 'Start date'}))
    date_fin = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'class': 'form-select form__input','type': 'date', 'placeholder': 'End date'}))

    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')

        if date_debut and date_fin and date_debut >= date_fin:
            raise forms.ValidationError("End date must be later than the start date.")
