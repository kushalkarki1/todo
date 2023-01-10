from django.urls import path
from todofeature.views import home

app_name = "todofeature"

urlpatterns = [
    path("", home, name="home"),
]