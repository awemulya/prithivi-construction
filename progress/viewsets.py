from rest_framework import viewsets
from progress.serializer import TaskSerializer, SiteProgressSerializer
from progress.models import Task
from project.models import Project


class SiteProgressViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = SiteProgressSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()