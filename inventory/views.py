from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Stock, DailyConsumption


@login_required
def stock_list(request):
    print("USER FACILITY:", request.user.facility)
    stocks = Stock.objects.filter(facility=request.user.facility)
    print("STOCK COUNT:", stocks.count())
    return render(request, "inventory/stock_list.html", {"stocks": stocks})


@login_required
def daily_consumption(request):
    stocks = Stock.objects.filter(facility=request.user.facility)

    if request.method == "POST":
        stock_id = request.POST.get("stock")
        quantity = int(request.POST.get("quantity"))
        remarks = request.POST.get("remarks")

        stock = get_object_or_404(Stock, id=stock_id)

        try:
            DailyConsumption.objects.create(
                facility=request.user.facility,
                stock=stock,
                quantity_consumed=quantity,
                remarks=remarks
            )
            messages.success(request, "Consumption recorded successfully")
            return redirect("daily_consumption")

        except ValueError as e:
            messages.error(request, str(e))

    return render(request, "inventory/daily_consumption.html", {"stocks": stocks})
