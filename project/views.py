from django.shortcuts import render


def dashboard(request):
    return render(request, 'home.html')


def employee_list(request):
    return render(request, 'home.html')
