from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inventory.models import Stock
from .models import Requisition


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
