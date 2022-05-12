from django.shortcuts import render, redirect
from carts.models import Cart, CartEntry
from addresses.models import Address

from .models import Order


# Create your views here.
def address_page(request):
    cart_id = request.session.get("cart_id", None)
    entries = CartEntry.objects.filter(cart__id=cart_id)
    user = request.user

    total = 0
    for entry in entries:
        subtotal = entry.sku_product.master.costo * entry.quantity
        total += subtotal

    addresses = Address.objects.filter(user=user)

    context = {
        "addresses": addresses,
        "entries": entries,
        "total": total,
    }

    form = request.POST
    if form:

        if form.get('address_id', False):
            request.session['address_id'] = form['address_id']
        else:
            nombre_completo = form['nombre_completo']
            calle_numero = form['calle_numero']
            codigo_postal = form['codigo_postal']
            estado = form['estado']
            ciudad = form['ciudad']
            colonia = form['colonia']
            telefono = form['telefono']
            pais = form['pais']

            same_address_qs = addresses.filter(
                nombre_completo=nombre_completo,
                calle_numero=calle_numero,
                codigo_postal=codigo_postal,
                estado=estado,
                ciudad=ciudad,
                colonia=colonia,
                telefono=telefono,
                pais=pais,
                user=request.user
            )

            if len(same_address_qs) == 1:
                address = same_address_qs.first()
            else:
                address = Address(
                    nombre_completo=nombre_completo,
                    calle_numero=calle_numero,
                    codigo_postal=codigo_postal,
                    estado=estado,
                    ciudad=ciudad,
                    colonia=colonia,
                    telefono=telefono,
                    pais=pais,
                    user=request.user
                )
                address.save()

            request.session['address_id'] = address.id

        return redirect('orders:confirm')

    return render(request, "orders/address.html", context)


def confirm_page(request):
    cart_id = request.session.get("cart_id", None)
    address_id = request.session.get("address_id", None)
    entries = CartEntry.objects.filter(cart__id=cart_id)

    total = 0
    for entry in entries:
        subtotal = entry.sku_product.master.costo * entry.quantity
        total += subtotal

    address = None
    address_qs = Address.objects.filter(id=address_id)
    if len(address_qs) == 1:
        address = address_qs.first()

    form = request.POST
    if form:
        order = Order(user=request.user, direccion_entrega=address)
        order.save()
        request.session['order_id'] = order.id
        for entry in entries:
            order.cart_entries.add(entry)

        request.session['cart_id'] = None
        return redirect('orders:created')

    context = {
        "address": address,
        "entries": entries,
        "total": total,
    }

    return render(request, "orders/confirm.html", context)


def created_page(request):
    order = None
    order_id = request.session.get("order_id")
    order_qs = Order.objects.filter(id=order_id)
    if len(order_qs) == 1:
        order = order_qs.first()

    print(order)
    context = {
        "order": order,
    }

    return render(request, "orders/created.html", context)
