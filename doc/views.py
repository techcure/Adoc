from django.shortcuts import render
from .forms import RegForm
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required


class IndexView(View):
# Create your views here.
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = RegForm(request.POST, request.FILES)
			if form.is_valid():
				post = form.save(commit=True)
				post.save()
				messages.success(request, 'Success!.')
			return render(request, 'doc/index.html', {'form': form})
		else:
			form = RegForm()
			queryset = Reg.objects.all()

		return render(request, 'doc/index.html', {'queryset':queryset, 'form':form})
	def get(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = RegForm(request.POST, request.FILES)
			if form.is_valid():
				post = form.save(commit=True)
				post.save()
				messages.success(request, 'Success!.')
			return render(request, 'doc/index.html', {'form': form})
		else:
			form = RegForm()
			queryset = Reg.objects.all()

		return render(request, 'doc/index.html', {'queryset':queryset, 'form':form})