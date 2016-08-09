from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.template import RequestContext
from django.contrib import auth
from .models import *


def home(request):
	menu = 'disabled'
	queryset = BeneficiariesOffshores.objects.all()
	context = {
		"offshores_list" : queryset,
		"menu0": menu
	}
	return render(request, 'index.html', context)


def detail(request, id=None):
	instance = get_object_or_404(BeneficiariesOffshores, id = id)
	context = {
		"instance": instance
	}
	return render(request, 'detail.html', context, context_instance=RequestContext(request))

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login')

def faq(request):
	menu = 'disabled'
	return render(request, 'faq.html', {"menu1": menu})


