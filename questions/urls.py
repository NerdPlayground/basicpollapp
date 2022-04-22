from django.urls import path
from questions.views import home,question,vote,results

app_name= "questions"
urlpatterns= [
    path("",home,name="home"),
    path("question/<str:pk>/vote/",vote,name="vote"),
    path("question/<str:pk>/",question,name="question"),
    path('question/<str:pk>/results/',results,name="results")
]