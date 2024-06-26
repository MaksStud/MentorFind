from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import (CustomUserSerializerRead,
                          CustomUserSerializerEdit,
                          CustomUserTopSerializer,
                          CustomUserSerializerLogin)
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomUser
from django.db.models import Avg, Count
from rest_framework import status
from rest_framework.authtoken.models import Token
from advert.models import Advertisement


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


class CustomUserReadViaTokenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerRead

    def get(self, request, *args, **kwargs):
        token = request.headers.get('Authorization').split(' ')[1]
        token_obj = Token.objects.get(key=token)
        user = token_obj.user
        serializer = self.get_serializer(instance=user)
        return Response(serializer.data)


class CustomUserEditViewSet(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerEdit
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        token = request.headers.get('Authorization').split(' ')[1]

        try:
            token_obj = Token.objects.get(key=token)
            user = token_obj.user
        except Token.DoesNotExist:
            return Response({"detail": "Invalid token header. No credentials provided."},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(user, data=request.data)
        new_username = request.data.get("username", None)
        new_email = request.data.get("email", None)
        new_photo = request.data.get("photo", None)
        serializer.is_valid(raise_exception=True)

        current_password = request.data.get("current_password", None)
        if current_password is None:
            return Response({"detail": "Current password is required."}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(current_password):
            return Response({"detail": "Incorrect old password."}, status=status.HTTP_400_BAD_REQUEST)

        if new_username is not None:
            user.username = new_username

        if new_email is not None:
            user.email = new_email

        if new_photo is not None: 
            user.photo = new_photo

        new_password = request.data.get("password", None)
        if new_password is not None:
            user.set_password(new_password)
        user.save()
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

class DeleteUserViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        user = request.user
        user_ads = Advertisement.objects.filter(author=user)
        user_ads.delete()
        user.delete()
        return Response({"detail": "User and related ads deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT)
