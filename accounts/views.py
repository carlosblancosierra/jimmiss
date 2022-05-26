from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.contrib.auth import get_user_model

from orders.models import Order
from skus.models import SkuMaster, SkuProduct
from marcas.models import Marca

User = settings.AUTH_USER_MODEL


def register_page_local(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register-local.html", context)


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
