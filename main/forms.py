from django.forms import ModelForm, TextInput, Textarea
from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "category",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "category": "Kategori Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Web Development",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "ended_at",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "ended_at": "Tanggal Selesai (Kosongkan jika masih berlangsung)",
        }

        widgets = {
            "title": TextInput(attrs={"placeholder": "Software Engineer Intern", "maxlength": 255}),
            "description": Textarea(attrs={"placeholder": "Ceritakan Pengalamanmu", "rows": 3}),
        }