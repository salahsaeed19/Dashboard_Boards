from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login as auth_login


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('Home')
        
    return render(request, 'user/signup.html', {'form': form})
