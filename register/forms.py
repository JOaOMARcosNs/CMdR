from django import forms

from .models import Homeless

class DateInput(forms.DateInput):
    input_type = 'date'

class HomelessForm(forms.ModelForm):
    class Meta:
        model = Homeless
        fields = 'frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight', 'blood_type', 'nationality', 'about'
        widgets = {'birth_date': DateInput()}

        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        #     'description': forms.Textarea(
        #         attrs={'placeholder': 'Enter description here'}),
        # }
        
        # placeholders = {
        #     'frist_name': 'awsdasdasdasdasd'
        # }
        # labels = {
        #     'frist_name' : '',
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class' : 'mask-cpf'})
        self.fields['rg'].widget.attrs.update({'class' : 'mask-rg'})
        


