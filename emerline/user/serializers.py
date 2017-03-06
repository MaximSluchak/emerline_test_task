from django.contrib.auth.models import User
from rest_framework import serializers

from emerline.project.models import Project
from emerline.task.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups',)


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = ('projectName', 'users',)


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer
    projects = ProjectSerializer

    class Meta:
        model = Task
        fields = ('title', 'description', 'dueDate', 'user', 'projects',)
