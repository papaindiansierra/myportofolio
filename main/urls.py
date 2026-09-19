from django.urls import path
from main.views import (
    show_main,
    show_experience,
    get_experience_json,
    create_experience,
    edit_experience,
    delete_experience,
    show_project,
    create_project,
    get_projects_json,
    delete_project,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    # experience URLs
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/edit/<uuid:experience_id>/", edit_experience, name="edit_experience"),
    path("experience/delete/<uuid:experience_id>/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    
    # project URLs
    path("projects/", show_project, name="show_project"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
]