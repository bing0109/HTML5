from django.shortcuts import render

# Create your views here.


def index(request):
    print('1111')
    return render(request, 'index.html')

