from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, TextInput
from django.utils.html import strip_tags
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

  def clean_title(self):
    title = strip_tags(self.cleaned_data["title"]).strip()
    if not title:
      raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
    return title

  def clean_category(self):
    return strip_tags(self.cleaned_data["category"]).strip()

  def clean_description(self):
    return strip_tags(self.cleaned_data["description"]).strip()


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