from django.shortcuts import render, redirect
from .forms import TripForm
from .models import Trip

def trip_request_view(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trip_dashboard')
    else:
        form = TripForm()
    trips = Trip.objects.all()
    return render(request, 'trips/dashboard.html', {'form': form, 'trips': trips})

