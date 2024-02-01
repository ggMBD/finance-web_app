from django.shortcuts import render
from expense.models import Expense
from django.contrib.auth.decorators import login_required
from expense.forms import ExpenseForms
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect


@login_required
def all(request):

	return render(request,'allexpenses.html',{'expenses' : Expense.objects.filter(user=request.user)})




@login_required
def expense(request, expense_id):

	exp = Expense.objects.get(id=expense_id)
	u = request.user




	if request.method == "POST":
		fk = ExpenseForms(request.POST,instance=exp)
		if fk.is_valid():
			fk.save()
			
			return HttpResponseRedirect('/expenses/',{'expenses' : Expense.objects.filter(user=request.user)})

	else: 
		fk = ExpenseForms(instance=exp)

	arg = {}
	arg.update(csrf(request))
	arg['form'] = fk
	arg['expense']= exp

	return render(request, 'expense.html', arg)



def delete(request, expense_id):
	Expense.objects.get(id=expense_id).delete()
	
	
	return render(request, 'allexpenses.html',{'expenses' : Expense.objects.filter(user=request.user)})





def add(request):
	
	u = request.user

	if request.method == "POST":
		fk = ExpenseForms(request.POST)
		if fk.is_valid():
			inc = fk.save(commit = False)
			inc.user = u
			inc.save()


			return HttpResponseRedirect('/expenses/')

	else: 
		fk = ExpenseForms()

	arg = {}
	arg.update(csrf(request))
	arg['user']=u
	arg['form'] = fk


	return render(request, 'add_expense.html', arg)