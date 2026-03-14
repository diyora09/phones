from django.shortcuts import render

from phones.models import Phones


# Create your views here.



def details(request, phone_id):
    phone = Phones.objects.get(id=phone_id)
    context = {
        'phone':phone
    }
    return render(request, 'detailes.html', context)

def phones(request):
    phones = Phones.objects.all()
    context = {
        'phones':phones
    }
    return render(request, 'phones.html', context)
