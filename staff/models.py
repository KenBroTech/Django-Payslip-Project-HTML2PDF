from django.db import models

# Create your models here.


class SalaryRate(models.Model):
    position = models.CharField(max_length=100)
    basic_salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    hours = models.PositiveIntegerField(default=0)
    salary_rate = models.ForeignKey(SalaryRate, on_delete=models.CASCADE)
    gross_salary = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.gross_salary = (self.hours * self.salary_rate.basic_salary)
        return super().save(*args, **kwargs)
