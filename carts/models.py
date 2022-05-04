from django.db import models
from django.conf import settings
from skus.models import SkuProduct

User = settings.AUTH_USER_MODEL


# Create your models here.
class CartsManager(models.Manager):
    def new_or_get(self, request):

        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id).filter(active=True)

        if qs.count() == 1:
            new_object = False
            cart_obj = qs.first()

            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_object = True
            request.session['cart_id'] = cart_obj.id

        return cart_obj, new_object

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user

        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    subtotal = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = CartsManager()

    def __unicode__(self):
        return "ID: {}. Total is ${}".format(self.id, self.total)


class CartEntryManager(models.Manager):
    def new(self, request, sku_product, quantity):
        cart_obj, new_cart = Cart.objects.new_or_get(request)
        return self.model.objects.create(sku_product=sku_product, cart=cart_obj, quantity=quantity)


class CartEntry(models.Model):
    sku_product = models.ForeignKey(SkuProduct, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)

    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CartEntryManager()

    def __unicode__(self):
        return "This entry contains {} {}(s). Total: {}.".format(self.quantity, self.sku_product.product, self.total)
