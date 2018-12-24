from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index1(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'index2.html')


