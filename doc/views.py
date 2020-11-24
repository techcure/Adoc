from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.views import View
from scripts.docson2 import docson
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


class JsonView(View):

	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form1 = FilesForm(request.POST,request.FILES)
			upload = request.FILES['upload']
			# import pdb;pdb.set_trace()

			if form1.is_valid():
				try:
					form1.save()
					return redirect("jtod")
				except:
					pass
			else:
				return render(request,'doc/jtod.html',{'form1' : form1})
		else:
			form1 = FilesForm()
		return render(request,'doc/jtod.html',{'form1' : form1})
	
	def get(self, request, *args, **kwargs):
		if request.method == 'POST':
			form1 = FilesForm(request.POST,request.FILES)
			if form1.is_valid():
					form1.save()
					return redirect("jtod")
			else:
				return render(request,'doc/jtod.html',{'form1' : form1})
		else:
			form1 = FilesForm()
		return render(request,'doc/jtod.html',{'form1' : form1})


class DocView(View):

	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = FileForm(request.POST,request.FILES)
			if form.is_valid():
				try:
					form.save()
					return redirect("dtoj")
				except:
					pass
			else:
				return render(request,'doc/dtoj.html',{'form' : form})
		else:
			form = FilesForm()
		return render(request,'doc/dtoj.html',{'form' : form})
	
	def get(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = FilesForm(request.POST,request.FILES)
			if form.is_valid():
				try:
					form.save()
					return redirect("dtoj")
				except:
					pass
			else:
				return render(request,'doc/dtoj.html',{'form' : form})
		else:
			form = FilesForm()
		return render(request,'doc/dtoj.html',{'form' : form})