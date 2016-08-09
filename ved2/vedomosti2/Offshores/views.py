from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.template import RequestContext
from django.contrib import auth
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


def home(request):
	menu = 'disabled'
	queryset_list = BeneficiariesOffshores.objects.all().order_by("offshore")
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(offshore__off_name__icontains=query) |
			Q(offshore__off_jurisdiction__icontains=query) |
			Q(beneficiary__ben_name__icontains=query) |
			Q(beneficiary__ben_lastname__icontains=query) |
			Q(share__icontains=query) |
			Q(source__icontains=query) 
			).distinct()

	paginator = Paginator(queryset_list, 5)
	page = request.GET.get("page")
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
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


