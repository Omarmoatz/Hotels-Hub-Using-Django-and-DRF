from rest_framework.response import Response
from rest_framework import viewsets

from accounts.models import User
from accounts.api.serializers import UserSerializer, UserDetailSerializer, UserCreateSerializer


class UserViewSetApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        
        if self.action in ['retrieve', 'update', 'partial_update']:
            return UserDetailSerializer
        
        return super().get_serializer_class()