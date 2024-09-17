from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm



def home_page(request):
    return render(request, "home.html")

def about_page(request):
    return render(request, "about.html")

@login_required
def profile_page(request):
    return render(request, 'profile_user.html')

def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,
                  'register.html',
                  {'form': UserRegisterForm()})
