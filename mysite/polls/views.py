from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('Я люблю майкрафт')
    return render(request, 'polls/index.html')
