from django.shortcuts import render

from main.models import Experience

def show_main(request):
    context = {
        "name": "Muhammad Hafidz Muazzam",
        "npm": "2506621812",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Fakultas Ilmu Komputer Universitas Indonesia "
            "yang tertarik pada pengembangan perangkat lunak dan sistem komputer."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Muhammad Hafidz Muazzam",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)