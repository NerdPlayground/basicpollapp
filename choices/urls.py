from django.urls import path
from choices.views import add_choice,edit_choice,delete_choice

app_name="choices"
urlpatterns= [
    path("add-choice/<str:pk>/",add_choice,name="add-choice"),
    path("edit-choice/<str:pk>/",edit_choice,name="edit-choice"),
    path("delete-choice/<str:pk>/",delete_choice,name="delete-choice"),
]