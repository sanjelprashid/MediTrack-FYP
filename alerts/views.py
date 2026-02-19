from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Alert


@login_required
def staff_alerts(request):
    alerts = Alert.objects.filter(
        stock__facility=request.user.facility
    ).order_by("-created_at")

    return render(request, "alerts/staff_alerts.html", {"alerts": alerts})

