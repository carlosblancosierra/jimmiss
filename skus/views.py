from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def detail_page(request, slug):
    sku_master = get_object_or_404(models.SkuMaster, slug=slug)

    sku_products = models.SkuProduct.objects.filter(master=sku_master)

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
                color_skus.append(sku_product)
        products[color.title] = color_skus

    print(products)

    context = {
        "obj": sku_master,
        "products": products,
    }

    return render(request, "skus/detail.html", context)
