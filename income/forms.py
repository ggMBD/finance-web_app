from django import forms
from income.models import Income

class IncomeForms(forms.ModelForm):

	class Meta:
		model = Income
		fields = ('item','amount','date')
		widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        