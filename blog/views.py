from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def start(request):
    return render(request, "blog/index.html")

def posts(request):
    return HttpResponse("posts")

def post_details(request, slug):
    return HttpResponse(slug)