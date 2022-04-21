from django.urls import path
from questions.views import all_questions,question

app_name= "questions"
urlpatterns= [
    path("all-questions/",all_questions,name="all-questions"),
    path("question/<str:pk>/",question,name="question")
]