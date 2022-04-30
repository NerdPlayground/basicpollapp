from django.urls import path
from users.views import (
    register_user,votes,
    login_user,logout_user,
)

app_name= "authentication"
urlpatterns=[
    path("register/",register_user,name="register-user"),
    path("login/",login_user,name="login-user"),
    path("votes/",votes,name="votes"),
    path("logout/",logout_user,name="logout-user"),
]