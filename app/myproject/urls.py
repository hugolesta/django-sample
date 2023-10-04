from django.urls import path
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Django from StackOverflow!")

urlpatterns = [
    path('', hello, name='hello'),
]
