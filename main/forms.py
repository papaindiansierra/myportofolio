from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput
from main.models import Experience, Project


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
        "title": TextInput(
            attrs={
                "placeholder": "Software Engineer Intern",
                "maxlength": 255,
            }
        ),
        "description": Textarea(
            attrs={"placeholder": "Ceritakan Pengalamanmu", "rows": 3}
        ),
    }


class CustomUserCreationForm(UserCreationForm):

  class Meta(UserCreationForm.Meta):
    model = User
    fields = ["username"]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["username"].help_text = None
    if "password1" in self.fields:
      self.fields["password1"].help_text = None
    if "password2" in self.fields:
      self.fields["password2"].help_text = None