from django.shortcuts import render


def dashboard(request):
    if request.user.user_site_manager():
        return render(request, 'base.html')
    else:
        return render(request, 'base_invalid.html')


def employee_list(request):
    if request.user.user_site_manager():
        return render(request, 'dashboard_index.html')
    else:
        return render(request, 'dashboard_invalid.html')
    return render(request, 'home.html')
