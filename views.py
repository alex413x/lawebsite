from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
	# return HttpResponse('Hello, world.  You\'re at the site index')
	return render(request, 'renaissance/index.html', {})

# def index(request):
# 	return HttpResponse('Hello')
