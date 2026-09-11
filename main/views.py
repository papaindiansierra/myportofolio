from django.shortcuts import render

from main.models import Experience, Project

def show_main(request):
    context = {
        "name": "Muhammad Hafidz Muazzam",
        "npm": "2506621812",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "CS student at Universitas Indonesia passionate about technology, especially in modern automotive instruments and features."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Muhammad Hafidz Muazzam",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_project(request):
    projects = Project.objects.all()
    context = {
        "name": "Muhammad Hafidz Muazzam",
        "short_name": "Hafidz",
        "project_list": projects,
    }
    return render(request, "projects.html", context)