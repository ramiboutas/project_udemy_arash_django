from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


def home(request):
    context = {}
    return render(request, 'home.html', context)
