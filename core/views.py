from django.shortcuts import render

from django.http import HttpResponse


def index_core(request):
    return render(request, "core/about.html", {"title": "Core_About"})
