from django.shortcuts import render
from .models import Contacto


# Create your views here.
def detail_page(request, contact_id):
    contact = None
    qs = Contacto.objects.filter(id=contact_id)

    if len(qs) == 1:
        contact = qs.first()

    context = {
        "contact": contact,
    }

    return render(request, "contactos/detail.html", context)


def home_page(request):
    qs = Contacto.objects.all()

    context = {
        "contactos": qs,
    }
    return render(request, "contactos/list.html", context)
