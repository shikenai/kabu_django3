from django.shortcuts import render
from stocks.my_modules import my_function


# Create your views here.
def index(request):
    my_function.hello()
    return render(request, 'index.html')
