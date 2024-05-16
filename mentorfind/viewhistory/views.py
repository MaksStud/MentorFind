from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ViewHistory
from .serializers import ViewHistorySerializer, ViewHistorySerializerWithAdvertisementData
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.templatetags.static import static
from django.utils import timezone


class ViewHistoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ViewHistory.objects.all()
    serializer_class = ViewHistorySerializer

    def create(self, request, *args, **kwargs):
        token_key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user = Token.objects.get(key=token_key).user

        advertisement_id = request.data.get('advertisement')
        existing_view_history = ViewHistory.objects.filter(user=user, advertisement_id=advertisement_id).first()

        if existing_view_history:
            existing_view_history.timestamp = timezone.now()
            existing_view_history.save()
            serializer = self.get_serializer(existing_view_history)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            request.data['user'] = user.pk
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                view_history_obj = serializer.save()
                if view_history_obj:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


    def delete_full_viewhistory(self, request, *args ,**kwargs):
        token_key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user = Token.objects.get(key=token_key).user
        ViewHistory.objects.filter(user=user).delete()
        return Response({'message': 'All view history deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class ViewHistoryViewGet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ViewHistory.objects.all()
    serializer_class = ViewHistorySerializerWithAdvertisementData

    def list(self, request, *args, **kwargs):
        token_key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user = Token.objects.get(key=token_key).user

        saved_view_history = ViewHistory.objects.filter(user=user)
        serializer = self.get_serializer(saved_view_history, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
