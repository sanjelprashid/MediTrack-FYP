from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inventory.models import Stock
from .models import Requisition
from django.shortcuts import get_object_or_404

@login_required
def create_requisition(request):
    stocks = Stock.objects.filter(facility=request.user.facility)

    if request.method == "POST":
        stock_id = request.POST.get("stock")
        quantity = int(request.POST.get("quantity"))

        stock = Stock.objects.get(id=stock_id)

        Requisition.objects.create(
            facility=request.user.facility,
            stock=stock,
            quantity_requested=quantity
        )

        messages.success(request, "Requisition submitted")
        return redirect("create_requisition")

    return render(request, "requisitions/create_requisition.html", {"stocks": stocks})

@login_required
def supervisor_requisitions(request):
    if request.user.role != "SUPERVISOR":
        return redirect("dashboard_router")

    requisitions = Requisition.objects.filter(status="PENDING").order_by("-created_at")

    return render(request, "requisitions/supervisor_requisitions.html", {
        "requisitions": requisitions
    })


@login_required
def approve_requisition(request, pk):
    if request.user.role != "SUPERVISOR":
        return redirect("dashboard_router")

    requisition = get_object_or_404(Requisition, id=pk)
    requisition.status = "APPROVED"
    requisition.save()

    return redirect("supervisor_requisitions")


@login_required
def reject_requisition(request, pk):
    if request.user.role != "SUPERVISOR":
        return redirect("dashboard_router")

    requisition = get_object_or_404(Requisition, id=pk)
    requisition.status = "REJECTED"
    requisition.save()

    return redirect("supervisor_requisitions")

@login_required
def vendor_requisitions(request):
    if request.user.role != "VENDOR":
        return redirect("dashboard_router")

    requisitions = Requisition.objects.filter(status="APPROVED").order_by("-created_at")

    return render(request, "requisitions/vendor_requisitions.html", {
        "requisitions": requisitions
    })


from inventory.models import Stock
from alerts.models import Alert

@login_required
def fulfill_requisition(request, pk):
    if request.user.role != "VENDOR":
        return redirect("dashboard_router")

    requisition = get_object_or_404(Requisition, id=pk)

    # Increase stock
    stock = requisition.stock
    stock.quantity_available += requisition.quantity_requested
    stock.save()

    # Resolve existing pending alert
    Alert.objects.filter(
        stock=stock,
        alert_status="PENDING"
    ).update(alert_status="RESOLVED")

    # Update requisition
    requisition.status = "FULFILLED"
    requisition.save()

    return redirect("vendor_requisitions")
