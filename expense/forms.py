from django import forms
from expense.models import Expense


class ExpenseForms(forms.ModelForm):

	class Meta:
		model = Expense
		fields = ('item','amount','date')
		widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
