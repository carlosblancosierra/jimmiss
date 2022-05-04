from django.shortcuts import render
from .models import Cart, CartEntry


# Create your views here.

def home_page(request):
    cart_id = request.session.get("cart_id", None)
    entries = CartEntry.objects.filter(cart__id=cart_id)

    context = {
        "entries": entries,
    }

    return render(request, "carts/home.html", context)

# def agregar_page(request):
#     product_id = request.POST.get('cart_entry_product', None)
#     quantity = request.POST.get('cart_entry_quantity', None)
#
#     print("product_id", product_id)
#     print("quantity", quantity)
#
#     cart_entry = CartEntry.objects.add_multiple(request, product_id=product_id, quantity=quantity)
#     print(cart_entry)
#
#     CartShipment.objects.update_entries(cart_entry=cart_entry)
#
#     return redirect("carts:home")
