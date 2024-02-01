from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from homebudget.forms import UserCreationForm
from django.db.models import Sum
from income.models import Income
from expense.models import Expense


def home(request):

    user = request.user
    if user is not None:
        if user.is_active:
            incomes = Income.objects.filter(user=request.user).aggregate(Sum('amount')).get('amount__sum')
            expenses = Expense.objects.filter(user=request.user).aggregate(Sum('amount')).get('amount__sum')

            balance = (incomes if incomes is not None else 0) - (expenses if expenses is not None else 0)


            return render(request,'home.html', {'balance' : balance })
        else:
            return render(request,'home.html')




def login(request):
    l = {}
    l.update(csrf(request))
    return render(request,'login.html', l)


def authorize(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth.login(request,user)
            return render(request, 'loggedin.html')

    else:
        return render(request, 'invalid.html')


def loggedin(request):
    return render(request, 'loggedin.html')


def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def invalid(request):
    return render(request,'invalid.html')

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return render(request,'success.html')

    arg =	{}
    arg.update(csrf(request))
    arg['form'] = UserCreationForm()
    
    return render(request,'register.html', arg)
