from django.shortcuts import render
from .models import Staff
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.


def index(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff,
    }
    return render(request, 'staff/index.html', context)


def staff_payslip(request, pk):
    staff = Staff.objects.get(id=pk)
    template_path = 'staff/staff_payslip.html'
    context = {
        'staff': staff
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="payslip.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    # return render(request, 'staff/staff_payslip.html', context)
