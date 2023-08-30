from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('submit_work')  # Redirect to your desired view after login
    return render(request, 'login.html')  # Updated template path


def logout_view(request):
    logout(request)
    # return redirect('accounts:login')  # Redirect to your login view
    return render(request, 'logout.html')
