from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .models import Product, Order, LineItem
from .forms import CartForm, CheckoutForm
from . import cart

# Create your views here.


def index(request):
    all_products = Product.objects.all()
    return render(request, "pay_module/index.html", {
                                    'all_products': all_products,
                                    })


def show_product(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('app:cart')

    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'pay_module/product_detail.html', {
                                            'product': product,
                                            'form': form,
                                            })


def show_cart(request):

    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)

    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    return render(request, 'pay_module/cart.html', {
                                            'cart_items': cart_items,
                                            'cart_subtotal': cart_subtotal,
                                            })


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            o = Order(
                name = cleaned_data.get('name'),
                email = cleaned_data.get('email'),
                postal_code = cleaned_data.get('postal_code'),
                address = cleaned_data.get('address'),
            )
            o.save()

            all_items = cart.get_all_cart_items(request)
            for cart_item in all_items:
                li = LineItem(
                    product_id = cart_item.product_id,
                    price = cart_item.price,
                    quantity = cart_item.quantity,
                    order_id = o.id
                )

                li.save()

            cart.clear(request)

            request.session['order_id'] = o.id

            messages.add_message(request, messages.INFO, 'Order Placed!')
            return redirect('app:process_payment')


    else:
        form = CheckoutForm()
        return render(request, 'pay_module/checkout.html', {'form': form})



def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'pay_module/process_payment.html', {'order': order})


@csrf_exempt
def payment_done(request):
    return render(request, 'pay_module/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'pay_module/payment_cancelled.html')
