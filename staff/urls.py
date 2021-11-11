from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='staff-index'),
    path('staff/payslip/<int:pk>/', views.staff_payslip, name='staff-payslip'),
]
