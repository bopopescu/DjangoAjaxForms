from rest_framework import viewsets
from .models import LocalUsers
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = LocalUsers.object.all()
    serializer_class = UserSerializer 