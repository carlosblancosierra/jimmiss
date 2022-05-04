from django.shortcuts import render, redirect
from .models import Cart, CartEntry


# Create your views here.

def home_page(request):
    cart_id = request.session.get("cart_id", None)
    entries = CartEntry.objects.filter(cart__id=cart_id)

    context = {
        "entries": entries,
    }

    return render(request, "carts/home.html", context)


def agregar_page(request):
    form = request.POST
    if form:
        for sku_product, quantity in form.items():
            if sku_product == "csrfmiddlewaretoken":
                continue
            CartEntry.objects.new_or_update(request, sku_product, quantity)

    return redirect("carts:home")


def delete_entry_page(request):
    form = request.POST
    if form:
        sku_product = form['delete-entry-sku']
        CartEntry.objects.new_or_update(request, sku_product, 0)

    return redirect("carts:home")
