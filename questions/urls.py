from django.urls import path
from questions.views import home,question

urlpatterns= [
    path("home/",home,name="home"),
    path("question/<str:pk>/",question,name="question")
]