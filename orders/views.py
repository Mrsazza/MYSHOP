from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def order_create(request):
    return render(request, 'orders/order/create.html', {'section': 'create'})