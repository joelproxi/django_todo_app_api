from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.
from .models import Task
from .serializers import TaskSerializer


class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

