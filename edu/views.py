from django.shortcuts import render


def index(request):
    return render(request, "edu/index.html")


def setup(request):
    return render(request, "edu/setup.html")


def database(request):
    return render(request, "edu/database.html")


def template(request):
    return render(request, "edu/template.html")
