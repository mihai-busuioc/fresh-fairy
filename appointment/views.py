from django.shortcuts import render, redirect

# Create your views here.


def appointment(request):
    """ A view to return the cart content page """
    if request.method == 'POST':
        return render(request, 'appointment/appointment.html')

    else:

        return render(request, 'appointment/appointment.html')
