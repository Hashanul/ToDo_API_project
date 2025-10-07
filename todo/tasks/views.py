from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from .permissions import user_permission



# Create your views here.

# 1. List of all Task, Create a new Task
class TaskCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, user_permission]

    def get_queryset(self):
        status = self.request.query_params.get('status')
        if status:
            return Task.objects.filter(user=self.request.user, status__iexact=status)
        return Task.objects.filter(user=self.request.user)
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

# 2. single task / update / delete
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)



# jwt & Djoser authentication.
