from django.shortcuts import render, get_object_or_404
from carts.models import CartEntry

from . import models


# Create your views here.
def detail_page(request, slug):
    sku_master = get_object_or_404(models.SkuMaster, slug=slug)

    sku_products = models.SkuProduct.objects.filter(master=sku_master)

    cart_id = request.session.get("cart_id", None)
    entrys = CartEntry.objects.filter(cart__id=cart_id)
    cart_btn_text = 'Agregar al carrito'
    if len(entrys) > 0:
        cart_btn_text = 'Actualizar carrito'

    # group colors
    colores = []
    for obj in sku_products:
        if not obj.color in colores:
            colores.append(obj.color)

    products = {}
    for color in colores:
        color_skus = []
        for sku_product in sku_products:
            if sku_product.color == color:
                quantity = 0
                entry = entrys.filter(sku_product=sku_product)
                if len(entry) == 1:
                    quantity = entry.first().quantity
                sku_product_dict = {'sku': sku_product, 'quantity': quantity}
                color_skus.append(sku_product_dict)
        products[color.title] = color_skus

    print(products)

    context = {
        "obj": sku_master,
        "products": products,
        "cart_btn_text": cart_btn_text,
    }

    return render(request, "skus/detail.html", context)
