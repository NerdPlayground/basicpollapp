from django.urls import path
from questions.views import (
    home,vote_question,vote,results,
    add_question,manage_question,
    edit_question,delete_question
)

app_name= "questions"
urlpatterns= [
    path("",home,name="home"),
    path("question/<str:pk>/vote/",vote,name="vote"),
    path("question/<str:pk>/",vote_question,name="question"),
    path("manage-question/<str:pk>/",manage_question,name="manage-question"),
    path('question/<str:pk>/results/',results,name="results"),
    path("add-question/",add_question,name="add-question"),
    path("edit-question/<str:pk>/",edit_question,name="edit-question"),
    path("delete-question/<str:pk>/",delete_question,name="delete-question"),
]