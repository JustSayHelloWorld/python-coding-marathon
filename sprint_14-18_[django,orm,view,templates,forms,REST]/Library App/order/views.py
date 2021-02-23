from django.shortcuts import render, redirect

from .models import *
from .forms import OrderForm
from datetime import datetime


def delete_order(request, order_id):

    if request.method=="POST":
        Order.delete_by_id(order_id)
        return redirect("/orders")


def index(request):
    orders = Order.objects.order_by('id')
    return render(
        request,
        'order/index.html',
        {'title': 'Заказы', 'orders': orders}
    )

def detail(request, order_id):
    order = Order.get_by_id(order_id)
    context = {
        'title': f'Номер заказа: {order.id}',
        'order': order
    }

    return render(
        request,
        'order/detail.html',
        context
    )


def edit_order(request, order_id):
    error = ""

    if request.method == "POST":
        form = OrderForm(request.POST, instance=Order.get_by_id(order_id))
        if form.is_valid():
            form.save()
            return redirect("/orders")
        else:
            error = "неверная форма"

    form = OrderForm(instance=Order.get_by_id(order_id))

    data = {
        'form': form,
        'error': error,
        'end_at': Order.get_by_id(order_id).end_at.strftime("%d.%m.%Y, %H:%M"),
        'plated_end_at': Order.get_by_id(order_id).plated_end_at.strftime("%m/%d/%Y, %H:%M:%S")
    }


    return render(
        request,
        'order/edit.html',
        data
    )


def add_order(request):
    error = ""
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/orders")
        else:
            error = "неверная форма"
    form = OrderForm()


    data = {
        'form': form,
        'error': error
    }

    return render(
        request,
        'order/create.html',
        data
    )

