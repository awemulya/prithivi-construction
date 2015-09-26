from django.http import JsonResponse
from django.shortcuts import render
from inventory.models import InventoryAccount


def next_account_no(request):
    ac_no =  InventoryAccount.get_next_account_no()
    return JsonResponse({'ac_no': ac_no})
