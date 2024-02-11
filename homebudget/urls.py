from django.urls import path, include
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('', views.home),

    path('accounts/authorize/', views.authorize),
    path('accounts/login/', views.login),
    path('accounts/loggedin/', views.loggedin),
    path('accounts/logout/', views.logout),
    path('accounts/invalid/', views.invalid),
    path('accounts/register/', views.register),

    path('incomes/', include('income.urls')),
    path('expenses/', include('expense.urls')),
]
