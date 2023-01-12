from django.urls import path, include
from todofeature.views import home, CategoryAPIView, TaskViewSet
from rest_framework.routers import DefaultRouter

app_name = "todofeature"

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("", home, name="home"),
    path("category-list/", CategoryAPIView.as_view(),name="category_list"),
    path("api/", include(router.urls)),
]