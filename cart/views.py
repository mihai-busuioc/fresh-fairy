from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from services.models import Services

# Create your views here.


def view_cart(request):
    """ A view to return the cart content page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add service to cart """

    service = get_object_or_404(Services, pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    date = request.POST['your_date']
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if date in cart[item_id]['items_by_date'].keys():
            cart[item_id]['items_by_date'][date] += quantity
            messages.success(
                request, f'Updated {service.name} quantity to your cart')
        else:
            cart[item_id]['items_by_date'][date] = quantity
            messages.success(
                request, f'Added {service.name} to your cart')
    else:
        cart[item_id] = {'items_by_date': {date: quantity}}
        messages.success(
            request, f'Added {service.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the service in cart """

    service = get_object_or_404(Services, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    date = None
    if 'your_date' in request.POST:
        date = request.POST['your_date']
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if quantity > 0:
            cart[item_id]['items_by_date'][date] = quantity
            messages.success(
                request, f'Updated {service.name} quantity to your cart')
        else:
            del cart[item_id]['items_by_date'][date]
            if not cart[item_id]['items_by_date']:
                cart.pop(item_id)
            messages.success(request, f'Removed {service.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the service from cart """

    try:
        service = get_object_or_404(Services, pk=item_id)
        date = request.POST['your_date']
        cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            del cart[item_id]['items_by_date'][date]
            if not cart[item_id]['items_by_date']:
                cart.pop(item_id)
            messages.success(request, f'Removed {service.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing {e} item')
        return HttpResponse(status=500)
