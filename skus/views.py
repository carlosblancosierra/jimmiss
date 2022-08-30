from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from carts.models import CartEntry
from divisiones.models import Division
from categorias.models import Categoria

from .models import SkuMaster, SkuProduct
import unidecode


# Create your views here.
def detail_page(request, slug):
    sku_master = get_object_or_404(SkuMaster, slug=slug)

    sku_products = SkuProduct.objects.filter(master=sku_master)

    cart_id = request.session.get("cart_id", None)
    entrys = CartEntry.objects.filter(cart__id=cart_id, sku_product__master=sku_master)
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
        pictures.append(sku_master.image_4)
    if sku_master.image_5:
        pictures.append(sku_master.image_5)
    if sku_master.image_6:
        pictures.append(sku_master.image_6)

    context = {
        "obj": sku_master,
        "products": products,
        "cart_btn_text": cart_btn_text,
        "pictures": pictures
    }

    return render(request, "skus/detail.html", context)


def list_page(request, division_code=None):
    masters = SkuMaster.objects.all()
    division = None
    category = None
    bg = "bg-blue"

    division_code = unidecode.unidecode(division_code)

    if division_code:
        division = Division.objects.filter(code=division_code).first()
        masters = masters.filter(division=division)

    category_code = request.GET.get('categoria', None)
    if category_code:
        category = Categoria.objects.filter(code=category_code).first()
        masters = masters.filter(categoria=category)

    if division_code == 'ninas' or division_code == 'dama':
        bg = "bg-red"

    paginator = Paginator(masters, 20)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "queryset": page_obj,
        "division": division,
        "category": category,
        "bg": bg,
    }

    return render(request, "skus/list.html", context)


def all_page(request):
    masters = SkuMaster.objects.all()
    paginator = Paginator(masters, 20)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "queryset": page_obj,
    }

    return render(request, "skus/all.html", context)
