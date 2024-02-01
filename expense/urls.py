from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name='all'),
    path('<int:expense_id>/', views.expense, name='expense'),
    path('delete/<int:expense_id>/', views.delete, name='delete'),
    path('add/', views.add, name='add'),
]
