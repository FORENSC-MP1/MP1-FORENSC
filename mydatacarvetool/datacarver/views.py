from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    return HttpResponse("Hello, world. You're at the polls index page.")