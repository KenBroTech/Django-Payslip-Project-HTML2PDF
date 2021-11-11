from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('payslip/<int:pk>/', views.payslip, name='dashboard-payslip'),
]
