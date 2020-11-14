from django.shortcuts import render
from .forms import RegForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def registration(request):
	if request.method == 'POST':
		form = RegForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=True)
			post.save()
			messages.success(request, 'Success!.')
		return render(request, 'doc/registration.html', {'form': form})
	else:
			form = RegForm()
			queryset = Reg.objects.all()
			
			context = {'data':queryset, 'form':form}
	return render(request, 'doc/registration.html', context)

# def audio(request):
# 	if request.method == 'POST':
# 		form1 = AudioForm(request.POST, request.FILES)
# 		if form1.is_valid():
# 			post = form1.save(commit=True)
# 			post.save()
# 			messages.success(request, 'Success!.')
# 		return render(request, 'doc/registration.html', {'form1': form1})
# 	else:
# 			form = AudioForm()
# 			queryset = Word.objects.all()
			
# 			context = {'data':queryset, 'form':form}
# 	return render(request, 'doc/registration.html', context)