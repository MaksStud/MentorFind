from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import (CustomUserSerializerRead,
                          CustomUserSerializerEdit,
                          CustomUserSerializerLogin,
                          CustomUserTopSerializer)
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomUser
from django.db.models import Avg, Count



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


class TopUsersViewSet(viewsets.ViewSet):
    serializer_class = CustomUserTopSerializer

    def list(self, request):
        # Get all users along with the average rating and the number of their ads
        users_with_avg_rating_and_count = CustomUser.objects.annotate(
            avg_rating=Avg('review__rating'),
            advertisement_count=Count('advertisement')
        )

        # Sort them by average score and then by number of ads
        sorted_users = sorted(users_with_avg_rating_and_count, key=lambda x: (x.avg_rating if x.avg_rating is not None else -float('inf'), -x.advertisement_count), reverse=True)

        # Serialize the sorted list of users and return it
        serializer = self.serializer_class(sorted_users, many=True)
        return Response(serializer.data)