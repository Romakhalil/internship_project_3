from django.shortcuts import render,HttpResponse
from django import forms
from django.shortcuts import render
from .models import Intern
from .forms import TaskForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def home_page(request):
    # return HttpResponse('<b>Hello Interns<b>')
    return render(request, 'home.html')
# Create your views here.
@login_required
def submit_work(request):
    interns = Intern.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect or display a success message
            return HttpResponseRedirect('/success/')
    else:
        form = TaskForm()
        print('internlist',interns)
    
    return render(request, 'home.html', {'form': form, 'interns': interns})
@login_required
def Success(request):
    # return HttpResponse('<b>Hello Interns<b>')
    return render(request, 'success.html')