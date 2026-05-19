from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.save(created_by=self.request.user)

        #send_mail(
           # "New Task Assigned",
           # f"You have been assigned task: {task.title}",
           # settings.EMAIL_HOST_USER,
           # [task.assigned_to],
          #  fail_silently=False,
       # )


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]