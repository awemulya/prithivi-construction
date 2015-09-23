from rest_framework import viewsets
from user.models import AweUser
from user.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = AweUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
            serializer.save()
