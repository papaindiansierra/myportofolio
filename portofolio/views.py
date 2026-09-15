from django.shortcuts import render
from main.models import Project 

def landing_page(request):
    context = {
        "name": "Muhammad Hafidz Muazzam",
        "project_list": Project.objects.all(),
    }
    return render(request, "index.html", context)