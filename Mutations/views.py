from django.shortcuts import render,redirect
from .login import UserLogin
from .mutation import MutationEntry
from .models import Register, Mutation
from django.contrib import messages
import datetime

def index(request):
    if request.method == 'POST':
        form = Register.objects.get(userName = request.method['name'])
        if form.password == request.POST['password']:
            request.session['id']=form.id
            messages.success(request,('Succesfully Logged In'))
            return redirect('report')
    else:
        return render(request, 'home.html',{}) 

def register(request):
    return render(request,'register.html',{})

def home(request):
    return render(request,'home.html',{})

def report(request):
    return render(request, 'report.html',{})

def entry(request):
    return render(request,'entry.html',{})