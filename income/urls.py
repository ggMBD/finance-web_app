from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name='all'),
    path('<int:income_id>/', views.income, name='income'),
    path('delete/<int:income_id>/', views.delete, name='delete'),
    path('add/', views.add, name='add'),
]
