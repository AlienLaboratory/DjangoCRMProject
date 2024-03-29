from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from . models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    #verify if user is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully logged in")
            return redirect('home')
        else:
            messages.success(request,"Could not log in, try again?")
            return redirect('home')
    else:
        return render(request, 'home.html',{'records':records})

def login_user(request):
    pass


def logout_user(request):
     logout(request)
     messages.success(request, "Successfully logged out")
     return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, "Successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})

#pk = primary_key
def show_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "Please login first!")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record has been deleted!")
        return redirect('home')
    else:
        messages.success(request, "Please login first!")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid:
                add_record = form.save()
                messages.success(request, "Record Added Successfully!")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Login First!")
        return redirect('home')


def update_record(request, pk):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if request.method == "POST":
            if form.is_valid:
                form.save()
                messages.success(request, "Record Updated Successfully!")
                return redirect('home')
        return render(request, 'update_record.html', {'form':form,'record':current_record})
    else:
        messages.success(request, "Login First!")
        return redirect('home')