from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomUserSerializerRead, CustomUserSerializerEdit
from .models import CustomUser
from rest_framework.generics import RetrieveUpdateAPIView



class CustomUserReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerRead

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


class CustomUserEditViewSet(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerEdit
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        '''
        Go to /users/edit/id/ where id is an integer
        '''
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
