from django.shortcuts import render

def index (request):
    return render(request,"bacs350/index.html")

def about (request):
    return render(request,"bacs350/about.html")