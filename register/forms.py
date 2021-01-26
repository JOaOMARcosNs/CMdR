from django import forms

from .models import Homeless

class DateInput(forms.DateInput):
    input_type = 'date'

class HomelessForm(forms.ModelForm):
    class Meta:
        model = Homeless
        fields = '__all__'
        widgets = {'birth_date': DateInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class' : 'mask-cpf'})
        self.fields['rg'].widget.attrs.update({'class' : 'mask-rg'})
        
