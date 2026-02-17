from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard_router")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


# 🔀 Central Router
@login_required
def dashboard_router(request):
    user = request.user

    if user.role == "STAFF":
        return redirect("staff_dashboard")
    elif user.role == "SUPERVISOR":
        return redirect("supervisor_dashboard")
    elif user.role == "VENDOR":
        return redirect("vendor_dashboard")
    elif user.role == "ADMIN":
        return redirect("/admin/")
    else:
        return redirect("login")


# 🏥 STAFF DASHBOARD (V1)
@login_required
def staff_dashboard(request):
    return render(request, "users/staff_dashboard.html")


# (We will implement these properly in V2)
@login_required
def supervisor_dashboard(request):
    return render(request, "users/supervisor_dashboard.html")


@login_required
def vendor_dashboard(request):
    return render(request, "users/vendor_dashboard.html")
