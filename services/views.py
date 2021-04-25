from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Services
from .forms import ServicesForm

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

    services = get_object_or_404(Services, pk=services_id)

    context = {
        'service': services,
    }

    return render(request, 'services/service_detail.html', context)


def add_service(request):
    """ Add a service to the store """
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully!')
            return redirect(reverse('add_service'))
        else:
            messages.error(
                request, 'Failed to add service. Please ensure form is valid!')
    else:
        form = ServicesForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_service(request, services_id):
    """ Edit a service in the store """
    service = get_object_or_404(Services, pk=services_id)
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(
                request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = ServicesForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)
