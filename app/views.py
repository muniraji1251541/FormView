from django.shortcuts import render
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.


class Django_form_page(FormView):
	template_name='Django_form_page.html'
	form_class=Djando_form

	def form_valid(self,form):
		d=form.cleaned_data
		return HttpResponse(str(d))


class Model_form_page(FormView):
	template_name='Model_form_page.html'
	form_class=Model_form

	def form_valid(self, form):
		form.save()
		return HttpResponse('Your data is submitted successfully')



	