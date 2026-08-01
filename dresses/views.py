from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Dress
from .forms import DressForm

# --- Public Views ---

def home_view(request):
   
    return render(request, 'home.html')


def signup_view(request):
   
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dress_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dress_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
   
    logout(request)
    return redirect('login')


# --- Protected CRUD Views ---

@login_required
def dress_list(request):
   
    dresses = Dress.objects.all()
    return render(request, 'dress_list.html', {'dresses': dresses})


@login_required
def add_dress(request):
  
    if request.method == 'POST':
        form = DressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dress_list')
    else:
        form = DressForm()
    return render(request, 'add_dress.html', {'form': form})


@login_required
def edit_dress(request, pk):
   
    dress = get_object_or_404(Dress, pk=pk)
    if request.method == 'POST':
        form = DressForm(request.POST, instance=dress)
        if form.is_valid():
            form.save()
            return redirect('dress_list')
    else:
        form = DressForm(instance=dress)
    return render(request, 'edit_dress.html', {'form': form, 'dress': dress})


@login_required
def delete_dress(request, pk):
    
    dress = get_object_or_404(Dress, pk=pk)
    dress.delete()
    return redirect('dress_list')