from django.shortcuts import render, redirect
from django.templatetags.static import static
from .data import SKU, SKU_TEST, MARCAS, DIVISIONES, SERIES, COMPOSICIONES, COLORES, TALLAS
from skus.models import SkuMaster, SkuProduct
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify

from marcas.models import Marca
from divisiones.models import Division
from series.models import Serie
from composiciones.models import Composicion
from colores.models import Color
from tallas.models import Talla


def home_page(request):
    categories = [
        {
            "pic": static('images/dama.jpg'),
            "title": 'Dama',
            "buttons": [
                {
                    "text": "Pronto",
                    "link": "#",
                    "class": "bg-red",
                    "logo": static('images/jimm-logo.png')
                },
            ]
        },
        {
            "pic": static('images/dama.jpg'),
            "title": 'Caballero',
            "buttons": [
                # {
                #     "text": "Pijamas",
                #     "link": "/division/caballero",
                #     "class": "bg-blue",
                #     "logo": static('images/jimm-logo.png')
                # },
                {
                    "text": "Ropa Interior",
                    "link": "/skus/caballero?cat=ropa_interior",
                    "class": "bg-blue",
                    "logo": static('images/jimm-logo.png')
                }
            ]
        },
        {
            "pic": static('images/dama.jpg'),
            "title": 'Niña',
            "buttons": [
                # {
                #     "text": "Pijamas",
                #     "link": "#",
                #     "class": "bg-red",
                #     "logo": static('images/jimm-logo.png')
                # },
                {"text": "Ropa Interior",
                 "link": "/skus/niñas?cat=ropa_interior",
                 "class": "bg-red",
                 "logo": static('images/jimm-logo.png')
                 },
            ]
        },
        {
            "pic": static('images/dama.jpg'),
            "title": 'Niño',
            "buttons": [
                # {"text": "Pijamas",
                #  "link": "#",
                #  "class": "bg-blue",
                #  "logo": static('images/jimm-logo.png')
                #  },
                {"text": "Ropa Interior",
                 "link": "/skus/niños?cat=ropa_interior",
                 "class": "bg-blue",
                 "logo": static('images/jimm-logo.png'),
                 }
                ,
            ]
        },
        {
            "pic": static('images/dama.jpg'),
            "title": 'Preescolar',
            "buttons": [
                # {"text": "Pijamas",
                #  "link": "#",
                #  "class": "bg-lblue",
                #  "logo": static('images/jimm-logo.png')
                #  },
                {
                    "text": "Ropa Interior",
                    "link": "/skus/preescolar?cat=ropa_interior",
                    "class": "bg-lblue",
                    "logo": static('images/jimm-logo.png')
                },

            ]
        },
        {
            "pic": static('images/dama.jpg'),
            "title": 'Bebé',
            "buttons": [
                # {"text": "Pijamas",
                #  "link": "#",
                #  "class": "bg-lblue",
                #  "logo": static('images/jimm-logo.png')
                #  },
                {
                    "text": "Ropa Interior",
                    "link": "/skus/bebe?cat=ropa_interior",
                    "class": "bg-lblue",
                    "logo": static('images/jimm-logo.png')
                },
                # {
                #     "text": "Accesorios",
                #     "link": "#",
                #     "class": "bg-lblue",
                #     "logo": static('images/jimm-logo.png')
                # },
                # {"text": "Pijamas",
                #  "link": "#",
                #  "class": "bg-lblue2",
                #  "logo": static('images/jimm-logo.png')
                #  },
                {
                    "text": "Ropa Interior",
                    "link": "/skus/bebe?cat=ropa_interior",
                    "class": "bg-lblue2",
                    "logo": static('images/jimm-logo.png')
                },
                # {
                #     "text": "Accesorios",
                #     "link": "#",
                #     "class": "bg-lblue2",
                #     "logo": static('images/jimm-logo.png')
                # },
            ]
        },

    ]

    context = {
        "categories": categories,
    }

    return render(request, "home.html", context)


def division_page(request):
    products = [
        {
            "sku": "909501BLACH",
            "marca": "JIM",
            "division": "CABALLERO",
            "descripcion": "Camiseta Tirantes",
            "serie": "JIM ACTIVE",
            "composicion": "Algodón 100%",
            "color": "BLANCO",
            "talla": "CHICA",
            "costo": "81",
            "precio": "135",
        }
    ]

    repeat = range(12)

    context = {
        "products": products,
        "repeat": repeat,
    }

    return render(request, "division.html", context)


def nosotros_page(request):
    context = {}

    return render(request, "nosotros.html", context)


def cart_page(request):
    products = [
        {
            "sku": "909501BLACH",
            "marca": "JIM",
            "division": "CABALLERO",
            "descripcion": "CAMISETA TIRANTES",
            "serie": "JIM ACTIVE",
            "composicion": "Algodón 100%",
            "color": "BLANCO",
            "talla": "CHICA",
            "costo": "81",
            "precio": "135",
        }
    ]

    repeat = range(4)

    context = {
        "products": products,
        "repeat": repeat,
    }

    return render(request, "cart.html", context)


def product_page(request):
    obj = [
        {
            "sku": "909501BLACH",
            "marca": "JIM",
            "division": "CABALLERO",
            "descripcion": "CAMISETA TIRANTES",
            "serie": "JIM ACTIVE",
            "composicion": "Algodón 100%",
            "color": "BLANCO",
            "talla": "CHICA",
            "costo": "81",
            "precio": "135",
        }
    ]

    tallas = [
        "Ch",
        "M",
        "G",
        "XG"
    ]

    repeat = range(4)

    context = {
        "obj": obj[0],
        "repeat": repeat,
        "tallas": tallas,
    }

    return render(request, "producto.html", context)


@staff_member_required
def data_page(request):
    for key, values in SKU_TEST.items():
        sku_master_qs = SkuMaster.objects.filter(sku=key)
        if len(sku_master_qs) == 0:
            sku = key
            descripcion = values['DESCRIPCION']
            costo = values['COSTO']
            precio = values['PRECIO']

            marca_title = values['MARCA']
            marca_qs = Marca.objects.filter(title=marca_title)
            marca_obj = None
            if len(marca_qs) == 1:
                marca_obj = marca_qs.first()
            else:
                raise ObjectDoesNotExist

            division_title = values['DIVISION']
            division_qs = Division.objects.filter(title=division_title)
            division_obj = None
            if len(division_qs) == 1:
                division_obj = division_qs.first()
            else:
                raise ObjectDoesNotExist

            serie_title = values['SERIE']
            serie_qs = Serie.objects.filter(title=serie_title)
            serie_obj = None
            if len(serie_qs) == 1:
                serie_obj = serie_qs.first()
            else:
                raise ObjectDoesNotExist

            composicion_title = values['COMPOSICION']
            composicion_qs = Composicion.objects.filter(title=composicion_title)
            composicion_obj = None
            if len(composicion_qs) == 1:
                composicion_obj = composicion_qs.first()
            else:
                raise ObjectDoesNotExist

            slug = slugify(sku
                           + "-" + division_title
                           + "-" + marca_title
                           + "-" + descripcion
                           + "-" + serie_title)

            new_sku_master = SkuMaster(sku=sku,
                                       descripcion=descripcion,
                                       costo=costo,
                                       precio=precio,
                                       marca=marca_obj,
                                       division=division_obj,
                                       serie=serie_obj,
                                       composicion=composicion_obj,
                                       slug=slug
                                       )
            new_sku_master.save()

    context = {
        "SKU": SKU
    }
    return render(request, "data.html", context)


@staff_member_required
def sku_products_page(request):
    for key, values in SKU.items():
        colores = values['COLORES']
        # print(colores)

        for color_title in colores:
            # print(color_title)
            tallas = colores[color_title]['TALLAS']
            # print(tallas)

            color_qs = Color.objects.filter(title=color_title)
            if len(color_qs) == 1:
                color_obj = color_qs.first()
            else:
                raise ObjectDoesNotExist

            master_sku_qs = SkuMaster.objects.filter(sku=key)
            if len(master_sku_qs) == 1:
                master_sku_obj = master_sku_qs.first()
            else:
                raise ObjectDoesNotExist

            for talla_title in tallas:

                talla_qs = Talla.objects.filter(title=talla_title)
                if len(talla_qs) == 1:
                    talla_obj = talla_qs.first()
                else:
                    raise ObjectDoesNotExist

                sku_product_qs = SkuProduct.objects.filter(
                    master=master_sku_obj,
                    color=color_obj,
                    talla=talla_obj
                )

                if len(sku_product_qs) == 0:
                    new_sku_product = SkuProduct(
                        master=master_sku_obj,
                        color=color_obj,
                        talla=talla_obj
                    )

                    new_sku_product.save()

    context = {
        "SKU": SKU
    }
    return render(request, "data.html", context)


@staff_member_required
def create_tags_page(request):
    # MARCAS, DIVISIONES, SERIES, COMPOSICIONES, COLORES, TALLAS

    marcas_list = []
    for marca in MARCAS:
        marcas_qs = Marca.objects.filter(title=marca)
        if len(marcas_qs) == 0:
            new_marca = Marca(title=marca)
            new_marca.save()
            marcas_list.append(new_marca)

    divisiones_list = []
    for title in DIVISIONES:
        qs = Division.objects.filter(title=title)
        if len(qs) == 0:
            new_obj = Division(title=title)
            new_obj.save()
            divisiones_list.append(new_obj)

    series_list = []
    for title in SERIES:
        qs = Serie.objects.filter(title=title)
        if len(qs) == 0:
            new_obj = Serie(title=title)
            new_obj.save()
            series_list.append(new_obj)

    composiciones_list = []
    for title in COMPOSICIONES:
        qs = Composicion.objects.filter(title=title)
        if len(qs) == 0:
            new_obj = Composicion(title=title)
            new_obj.save()
            composiciones_list.append(new_obj)

    # {"TITLE": "BLANCO", "SKU_SUFIX": "BLA", "HEX": "#FFF"},

    colores_list = []
    for obj in COLORES:
        qs = Color.objects.filter(title=obj['TITLE'])
        if len(qs) == 0:
            new_obj = Color(title=obj['TITLE'], sku_sufix=obj['SKU_SUFIX'], hex=obj['HEX'])
            new_obj.save()
            colores_list.append(new_obj)

    print(colores_list)

    # {"TITLE": "8 AÑOS", "SKU_SUFIX": "08", "SHORT": "8 Años", "ORDER": 8},

    tallas_list = []
    for obj in TALLAS:
        qs = Talla.objects.filter(title=obj['TITLE'])
        if len(qs) == 0:
            new_obj = Talla(
                title=obj['TITLE'],
                sku_sufix=obj['SKU_SUFIX'],
                short=obj['SHORT'],
                order=obj['ORDER'],
            )
            new_obj.save()
            tallas_list.append(new_obj)

    print(tallas_list)

    context = {
        "marcas_list": marcas_list,
        "divisiones_list": divisiones_list,
        "series_list": series_list,
        "composiciones_list": composiciones_list,
        "colores_list": colores_list,
        "tallas_list": tallas_list,

    }
    return render(request, "data.html", context)
