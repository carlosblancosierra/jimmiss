from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import messages

from orders.models import Order
from addresses.models import Address

from skus.models import SkuMaster, SkuProduct
from marcas.models import Marca
from .models import UserDetails
from .forms import CustomUserCreationForm, UserDetailsForm

User = settings.AUTH_USER_MODEL


# def register_page_local(request):
#     form = UserCreationForm(request.POST or None)
#     print(form)
# if form:
#     full_name = form.data['full_name']
#     nombre_comercial = form.data['nombre_comercial']
#     razon_social = form.data['razon_social']
#     telefono = form.data['telefono']
#     email = form.data['email']
#     password1 = form.data['password1']
#     password2 = form.data['password1']
#
#     # print('full_name: ', full_name)
#     # print('nombre_comercial: ', nombre_comercial)
#     # print('razon_social: ', razon_social)
#     # print('telefono: ', telefono)
#     # print('email: ', email)
#     # print('password1: ', password1)
#     # print('password2: ', password2)
#
#     user_obj = User(username=email,
#                     email=email,
#                     password=password1)
#
#     print(user_obj)
#
#     return redirect('/login')
# context = {"form": form}
# return render(request, "accounts/register-local.html", context)


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
    User = get_user_model()
    users = User.objects.all()[:5]

    skumasters = SkuMaster.objects.all()
    marcas = Marca.objects.all()

    context = {
        "orders": orders,
        "users": users,
        "skumasters": skumasters,
        "marcas": marcas,

    }
    return render(request, "accounts/staff-home.html", context)


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

            messages.success(request, 'Your profile was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserDetailsForm()
    return render(request, 'accounts/register-local.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
