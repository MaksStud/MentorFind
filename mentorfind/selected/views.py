from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Selected
from .serializers import SelectedSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.templatetags.static import static

class SelectedViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Selected.objects.all()
    serializer_class = SelectedSerializer

    def create(self, request, *args, **kwargs):
        token_key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        token = Token.objects.get(key=token_key)
        user = token.user
        advertisement_id = request.data.get('advertisement')

        existing_selected = Selected.objects.filter(user=user, advertisement_id=advertisement_id).exists()
        if existing_selected:
            return Response({'error': 'This ad has already been saved by a user'}, status=status.HTTP_403_FORBIDDEN)

        request.data['user'] = user.pk
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            viewobj = serializer.save()
            if viewobj:
                viewobj.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.filter_queryset(self.get_queryset().filter(user=user))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        advertisement_id = kwargs.get('pk')
        user = request.user
        selected_instance = get_object_or_404(Selected, user=user, advertisement_id=advertisement_id)
        self.perform_destroy(selected_instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def user_saved_ads(self, request):
        user = request.user
        selected_ads = Selected.objects.filter(user=user)
        ad_data = []
        for selected_ad in selected_ads:
            ad = selected_ad.advertisement
            ad_info = {
                'id': ad.id,
                'title': ad.title,
                'category': ad.category,
                'price': ad.price,
                'description': ad.description,
                'author': ad.author.id,
                'location': ad.location,
                'type_of_lesson': ad.type_of_lesson,
            }
            if ad.image:  # Check if the image exists
                ad_info['image'] = request.build_absolute_uri(ad.image.url)
            else:
                ad_info['image'] = static(settings.DEFAULT_AD_IMAGE)  # Provide a default image URL
            ad_data.append(ad_info)
        return Response(ad_data, status=status.HTTP_200_OK)