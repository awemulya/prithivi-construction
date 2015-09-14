from rest_framework.response import Response
from project.permissions import IsOwnerOrReadOnly
from user.models import AweUser

__author__ = 'awemulya'


from.models import Project
from .serializer import InChargeSerializer, SitesSerializer
from rest_framework import viewsets

class InChargeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = AweUser.objects.all()
    serializer = InChargeSerializer(queryset, many=True)

    def perform_create(self, serializer):
            serializer.save()


class SitesViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = SitesSerializer

    def perform_create(self, serializer):
            serializer.save()
