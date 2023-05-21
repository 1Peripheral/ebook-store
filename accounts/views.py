from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/sign_up.html', {'form':form})
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have successfully signed up .")
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
    
        else:
            return render(request, 'registration/sign_up.html', {'form':form})
    
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'registration/sign_up.html', {'form':form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')

        messages.error(request, "Invalid username or password")
        return render(request, 'registration/login.html', {'form':form})

def sign_out(request):
    logout(request) 
    return redirect('login')