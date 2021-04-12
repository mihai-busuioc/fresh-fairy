from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view to return the cart content page """

    return render(request, 'cart/cart.html')
