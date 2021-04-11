

def cart_contents(request):

    cart_items = []
    total = 0
    services_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'services_count': services_count,
    }

    return context
