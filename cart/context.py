from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Services


def cart_contents(request):

    cart_items = []
    total = 0
    services_count = 0
    cart = request.session.get('cart', {})

    for services_id, item_data in cart.items():
        service = get_object_or_404(Services, pk=services_id)
        total += item_data * service.price
        services_count += item_data
        cart_items.append({
            'services_id': services_id,
            'quantity': item_data,
            'service': service,
        })

    if total < settings.DISCOUNT_THRESHOLD:
        discount = 0
        discount_delta = total - settings.DISCOUNT_THRESHOLD
    else:
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
        discount_delta = 0

    grand_total = total - discount

    context = {
        'cart_items': cart_items,
        'total': total,
        'services_count': services_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,

    }

    return context
