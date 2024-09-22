from django.shortcuts import render

from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("Homepage")

def about_page_view(request):
    context = {
        "name": "Olorunfemi",
        "age": 35,

    }
    return render(request, "pages1/about.html", context)
