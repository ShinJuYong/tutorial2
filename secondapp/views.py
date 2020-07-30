from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

def show(request):
    curriculum = Hospital.objects.all()
    return render(request, 'hospital.html', {'list':curriculum})

    # html = ''
    # for c in curriculum:
    #     html += '%s %s %s %s %s %s %s<br>' % (c.sido, c.name, c.medical, c.room, c.tel, c.address)

    # return HttpResponse(html)
