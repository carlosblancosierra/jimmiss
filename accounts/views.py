from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import messages

from carts.models import Cart
from orders.models import Order
from addresses.models import Address

from categorias.models import Categoria
from colores.models import Color
from composiciones.models import Composicion
from divisiones.models import Division
from series.models import Serie
from tallas.models import Talla
from contactos.models import Contacto
from django.contrib.auth.decorators import login_required

from skus.models import SkuMaster, SkuProduct
from marcas.models import Marca
from .models import UserDetails
from .forms import CustomUserCreationForm, UserDetailsForm

User = settings.AUTH_USER_MODEL


# Create your views here.
def login_page(request):
    # future -> ?next=/articles/create/
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


# Create your views here.
@staff_member_required
def staff_home_page(request):
    orders = Order.objects.all()[:5]

    users = UserDetails.objects.all()[:5]

    skumasters = SkuMaster.objects.all()
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    colores = Color.objects.all()
    composiciones = Composicion.objects.all()
    divisiones = Division.objects.all()
    series = Serie.objects.all()
    tallas = Talla.objects.all()
    contactos = Contacto.objects.all()

    context = {
        "orders": orders,
        "users": users,
        "skumasters": skumasters,
        "marcas": marcas,
        "categorias": categorias,
        "colores": colores,
        "composiciones": composiciones,
        "divisiones": divisiones,
        "series": series,
        "tallas": tallas,
        "contactos": contactos,

    }
    return render(request, "accounts/staff-home.html", context)


@login_required
def home_page(request):
    user = request.user

    orders = Order.objects.filter(user=user)
    addresses = Address.objects.filter(user=user)

    user_details = None
    user_details_qs = UserDetails.objects.filter(user=user)
    if len(user_details_qs) == 1:
        user_details = user_details_qs.first()

    context = {
        "orders": orders,
        "addresses": addresses,
        "user": user,
        "user_details": user_details,

    }
    return render(request, "accounts/home.html", context)


@staff_member_required
def register_page_local(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST or None)
        profile_form = UserDetailsForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_obj = user_form.save()
            print(user_obj)

            nombre_comercial = profile_form.data['nombre_comercial']
            razon_social = profile_form.data['razon_social']
            telefono = profile_form.data['telefono']

            user_details_obj = UserDetails(user=user_obj,
                                           nombre_comercial=nombre_comercial,
                                           razon_social=razon_social,
                                           telefono=telefono,
                                           )

            user_details_obj.save()

            messages.success(request, 'Usuario creado con éxito')
            return redirect('/')
        else:
            messages.error(request, 'Error, por favor corrija la información')
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserDetailsForm()
    return render(request, 'accounts/register-local.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@staff_member_required
def detail_page(request, username):
    user = None
    user_detail = None
    orders = None

    # user_qs = User.objects.get(username=username)
    # if user_qs.exists():
    #     user = user_qs.first()

    user_details_qs = UserDetails.objects.filter(user__username=username)
    if user_details_qs.exists():
        user_detail = user_details_qs.first()

    orders = Order.objects.filter(user=user_detail.user)
    # carts = Cart.objects.filter(user=user_detail.user)
    addresses = Address.objects.filter(user=user_detail.user)

    context = {
        "user": user_detail,
        "orders": orders,
        # "carts": carts,
        "addresses": addresses,
    }
    return render(request, "accounts/detail.html", context)
