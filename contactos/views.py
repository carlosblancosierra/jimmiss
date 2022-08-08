from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Contacto


# Create your views here.
@staff_member_required
def detail_page(request, contact_id):
    contact = None
    qs = Contacto.objects.filter(id=contact_id)

    if len(qs) == 1:
        contact = qs.first()

    context = {
        "contact": contact,
    }

    return render(request, "contactos/detail.html", context)


@staff_member_required
def home_page(request):
    qs = Contacto.objects.all()

    context = {
        "contactos": qs,
    }
    return render(request, "contactos/list.html", context)
