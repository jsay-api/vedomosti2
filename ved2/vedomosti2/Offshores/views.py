from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth


def home(request):
	menu = 'disabled'
	return render(request, 'index.html', {"menu0": menu})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login')


