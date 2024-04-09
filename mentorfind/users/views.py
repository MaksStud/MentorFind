from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        '''
        :return:
            Returns the user by his id
            the path looks like this http://127.0.0.1:8000/users/get/{id}/
            where {id} is the number for example http://127.0.0.1:8000/users/get/1/
        '''
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
