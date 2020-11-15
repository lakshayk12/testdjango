from django.shortcuts import render
from .models import Destination
# Create your views here.


def home(request):
    dest1 = Destination()
    dest1.name = "Bali"
    dest1.price = 123
    dest1.desc = "Full of Adventure"
    return render(request, 'index.html', {'dest1': dest1})
