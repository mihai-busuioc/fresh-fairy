from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Services
from profiles.models import UserProfile


def cart_contents(request):

    cart_items = []
    total = 0
    services_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        service = get_object_or_404(Services, pk=item_id)
        for date, quantity in item_data['items_by_date'].items():
            total += quantity * service.price
            services_count += quantity
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'service': service,
                'date': date,
            })

    if total < settings.DISCOUNT_THRESHOLD:
        discount = 0
        discount_delta = settings.DISCOUNT_THRESHOLD - total
    else:
        if request.user.is_authenticated:
            discount = total * Decimal(settings.DISCOUNT_PERCENTAGE_USER / 100)
            discount_delta = 0
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
