from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.messages import info
from django.contrib.auth import logout as auth_logout
from user.forms import UserCreationForm


def index(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard_index.html')
    return login(request)


def web_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/app/dashboard/', **kwargs)
    else:
        if request.method == 'POST':
            if request.POST.get('remember_me', 'off') == 'on':
                request.session.set_expiry(1209600) # 2 weeks
            else:
                request.session.set_expiry(0)
        return login(request, **kwargs)


def logout(request, next_page=None):
    auth_logout(request)
    if next_page:
        return redirect(next_page)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            info(request, "Registration Complete Please Login To Continue.")
            return render(request, 'registration/login.html')
        return render(request, 'registration/register.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
