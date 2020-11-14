from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here. Handles http requests


def home(request):
    # data = {
    #     'name': 'Lakshay',
    # }
    # return JsonResponse(data)
    return render(request, 'home.html', {'name': 'Lakshay'})# HttpResponse("<h1>Hello World!</h1>")

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    sum = int(val1) + int(val2)
    return render(request, 'result.html', {'sum': sum})