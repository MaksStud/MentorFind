from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer, AppointmentListSerializer
from advert.models import Advertisement


class AppointmentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):

        def is_already_booked(student, advert):
            return Appointment.objects.filter(student=student, advert=advert).exists()

        student = request.user
        advert_id = request.data.get('advert')

        try:
            advert = Advertisement.objects.get(id=advert_id)
        except Advertisement.DoesNotExist:
            return Response({"detail": "Advertisement not found."}, status=status.HTTP_404_NOT_FOUND)

        mentor = advert.author

        if student == mentor:
            return Response({"detail": "You cannot create an appointment with yourself as a mentor."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Перевірка, чи студент вже записаний на це оголошення
        if is_already_booked(student, advert):
            return Response({"detail": "You are already booked for this advertisement."},
                            status=status.HTTP_400_BAD_REQUEST)

        appointment_data = {
            'student': student.id,
            'mentor': mentor.id,
            'advert': advert.id,
            'text': request.data.get('text')
        }

        serializer = self.get_serializer(data=appointment_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


class AppointmentListViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer

    def list(self, request, *args, **kwargs):
        mentor = request.user
        queryset = self.filter_queryset(self.get_queryset().filter(mentor=mentor))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)