from django.shortcuts import render
from income.models import Income
from django.contrib.auth.decorators import login_required
from income.forms import IncomeForms
from django.template.context_processors import csrf
from django.utils import timezone
from django.http import HttpResponseRedirect


@login_required
def all(request):

	return render(request,'all.html',{'incomes' : Income.objects.filter(user=request.user)})


@login_required
def income(request, income_id):

	inc = Income.objects.get(id=income_id)
	u = request.user




	if request.method == "POST":
		fk = IncomeForms(request.POST,instance=inc)
		if fk.is_valid():
			fk.save()
			return HttpResponseRedirect('/incomes/',{'incomes' : Income.objects.filter(user=request.user)})

	else: 
		fk = IncomeForms(instance=inc)

	arg = {}
	arg.update(csrf(request))
	arg['form'] = fk
	arg['income']= inc
	
	return render(request, 'income.html', arg)



def delete(request, income_id):
	Income.objects.get(id=income_id).delete()
	
	
	return render(request, 'all.html',{'incomes' : Income.objects.filter(user=request.user)})




def add(request):
	
	u = request.user

	if request.method == "POST":
		fk = IncomeForms(request.POST)
		if fk.is_valid():
			inc = fk.save(commit = False)
			inc.user = u
			inc.save()


			return HttpResponseRedirect('/incomes/')

	else: 
		fk = IncomeForms()

	arg = {}
	arg.update(csrf(request))
	arg['user']=u
	arg['form'] = fk


	return render(request, 'add_income.html', arg)