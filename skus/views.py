from django.shortcuts import render, get_object_or_404
from carts.models import CartEntry

from divisiones.models import Division
from .models import SkuMaster, SkuProduct


# Create your views here.
def detail_page(request, slug):
    sku_master = get_object_or_404(SkuMaster, slug=slug)

    sku_products = SkuProduct.objects.filter(master=sku_master)

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

    pictures = []
    if sku_master.image:
        pictures.append(sku_master.image)
    if sku_master.image_2:
        pictures.append(sku_master.image_2)
    if sku_master.image_3:
        pictures.append(sku_master.image_3)
    if sku_master.image_4:
        pictures.append(sku_master.image_3)
    if sku_master.image_5:
        pictures.append(sku_master.image_3)

    context = {
        "obj": sku_master,
        "products": products,
        "cart_btn_text": cart_btn_text,
        "pictures": pictures
    }

    return render(request, "skus/detail.html", context)


def list_page(request):
    masters = SkuMaster.objects.all()
    context = {
        "masters": masters,
    }

    return render(request, "skus/list.html", context)


def dama_page(request):
    masters = SkuMaster.objects.filter(division__code='dama')
    context = {
        "title": 'Dama',
        "masters": masters,
    }

    return render(request, "skus/list.html", context)


def caballero_page(request):
    masters = SkuMaster.objects.filter(division__code='caballero')
    context = {
        "title": 'Caballero',
        "masters": masters,
    }

    return render(request, "skus/list.html", context)


def ninas_page(request):
    masters = SkuMaster.objects.filter(division__code='ninas')
    context = {
        "title": 'Niñas',
        "masters": masters,
    }

    return render(request, "skus/list.html", context)


def ninos_page(request):
    masters = SkuMaster.objects.filter(division__code='ninos')
    context = {
        "title": 'Niños',
        "masters": masters,
    }

    return render(request, "skus/list.html", context)


def preescolar_page(request):
    masters = SkuMaster.objects.filter(division__code='preescolar')
    context = {
        "title": 'Preescolar',
        "masters": masters,
    }

    return render(request, "skus/list.html", context)


def bebe_page(request):
    masters = SkuMaster.objects.filter(division__code='bebe')
    context = {
        "title": 'Bebe',
        "masters": masters,
    }

    return render(request, "skus/list.html", context)
