from rest_framework import serializers
from todofeature.models import Category, Priority, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "created", "modified", ]


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ["name", "color_code", "created", "modified", ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "category", "priority", "is_done", "created", "modified"]