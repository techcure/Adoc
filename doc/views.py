from django.shortcuts import render
from .forms import RegForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
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