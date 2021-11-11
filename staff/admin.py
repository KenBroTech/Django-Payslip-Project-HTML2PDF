from django.contrib import admin
from .models import SalaryRate, Staff

# Register your models here.


class SalaryaRateAdmin(admin.ModelAdmin):
    list_display = ('position', 'basic_salary')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gross_salary')


admin.site.register(SalaryRate, SalaryaRateAdmin)
admin.site.register(Staff, StaffAdmin)
