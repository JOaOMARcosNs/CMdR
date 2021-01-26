from django import forms

from .models import Homeless

class HomelessForm(forms.ModelForm):
    class Meta:
        model = Homeless
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class' : 'mask-cpf'})
        self.fields['rg'].widget.attrs.update({'class' : 'mask-rg'})
        self.fields['birth_date'].widget.attrs.update({'class' : 'mask-birth_date'})
