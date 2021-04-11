from django.shortcuts import render, get_object_or_404
from .models import Services
# Create your views here.


def all_services(request):
    """ A view to show all the services page """

    services = Services.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, services_id):
    """ A view to show the detailed product """

    service = get_object_or_404(Services, pk=services_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)
