from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from todofeature.models import Category, Task
from todofeature.serializers import CategorySerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet
from todofeature.forms import TaskForm

def home(request):
    form = TaskForm()
    return render(request, "home.html", {"form": form})


class CategoryAPIView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
