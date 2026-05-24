from rest_framework import generics, permissions
from django.core.mail import send_mail
from django.conf import settings

from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.save(created_by=self.request.user)

        try:
            send_mail(
                subject="New Task Assigned",
                message=f"""
Hello,

A new task has been assigned to you.

Task Title: {task.title}
Description: {task.description}
Due Date: {task.due_date}

Thank you.
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[task.assigned_to],
                fail_silently=True,
            )
        except Exception as e:
            print("Email Error:", e)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]