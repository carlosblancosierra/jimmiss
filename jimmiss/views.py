from django.shortcuts import render, redirect
from django.templatetags.static import static
from .data import SKU


def home_page(request):
    categories = [
        {
            "pic": static('images/dama.jpg'),
            "title": 'Dama',
            "buttons": [
                {
                    "text": "Pijamas",
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
                {
                    "text": "Pijamas",
                    "link": "/division/caballero",
                    "class": "bg-blue",
                    "logo": static('images/jimm-logo.png')
                },
                {
                    "text": "Ropa Interior",
                    "link": "/division/caballero",
                    "class": "bg-blue",
                    "logo": static('images/jimm-logo.png')
                }
            ]
        },
        {
            "pic": static('images/dama.jpg'),
            "title": 'Niña',
            "buttons": [
                {
                    "text": "Pijamas",
                    "link": "#",
                    "class": "bg-red",
                    "logo": static('images/jimm-logo.png')
                },
                {"text": "Ropa Interior",
                 "link": "#",
                 "class": "bg-red",
                 "logo": static('images/jimm-logo.png')
                 },
            ]
        },
        {
            "pic": static('images/dama.jpg'),
            "title": 'Niño',
            "buttons": [
                {"text": "Pijamas",
                 "link": "#",
                 "class": "bg-blue",
                 "logo": static('images/jimm-logo.png')
                 },
                {"text": "Ropa Interior",
                 "link": "#",
                 "class": "bg-blue"}
                ,
            ]
        },
        {
            "pic": static('images/dama.jpg'),
            "title": 'Preescolar',
            "buttons": [
                {"text": "Pijamas",
                 "link": "#",
                 "class": "bg-lblue",
                 "logo": static('images/jimm-logo.png')
                 },
                {
                    "text": "Ropa Interior",
                    "link": "#",
                    "class": "bg-lblue",
                    "logo": static('images/jimm-logo.png')
                },

            ]
        },
        {
            "pic": static('images/dama.jpg'),
            "title": 'Bebé',
            "buttons": [
                {"text": "Pijamas",
                 "link": "#",
                 "class": "bg-lblue",
                 "logo": static('images/jimm-logo.png')
                 },
                {
                    "text": "Ropa Interior",
                    "link": "#",
                    "class": "bg-lblue",
                    "logo": static('images/jimm-logo.png')
                },
                {
                    "text": "Accesorios",
                    "link": "#",
                    "class": "bg-lblue",
                    "logo": static('images/jimm-logo.png')
                },
                {"text": "Pijamas",
                 "link": "#",
                 "class": "bg-lblue2",
                 "logo": static('images/jimm-logo.png')
                 },
                {
                    "text": "Ropa Interior",
                    "link": "#",
                    "class": "bg-lblue2",
                    "logo": static('images/jimm-logo.png')
                },
                {
                    "text": "Accesorios",
                    "link": "#",
                    "class": "bg-lblue2",
                    "logo": static('images/jimm-logo.png')
                },
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


def data_page(request):
    context = {
        "SKU": SKU
    }
    return render(request, "data.html", context)
