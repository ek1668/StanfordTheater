from django.shortcuts import render
from .models import Movie, Schedule
# Create your views here.

def about(request):

    dests = Movie.objects.all()
    schedules = Schedule.objects.all()

    all_times = Schedule.objects.all()
    return render(request, "about.html", {'dests': dests, 'schedules': schedules, "all_times": all_times})