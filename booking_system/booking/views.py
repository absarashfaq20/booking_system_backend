from rest_framework import viewsets, status, generics, serializers
from .models import Service, ServiceProvider, TimeSlot, Appointment
from .serializers import (
    ServiceSerializer,
    ServiceProviderSerializer,
    TimeSlotSerializer,
    AppointmentSerializer
)
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer


class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


# Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Signup View
class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        timeslot_id = request.data.get('timeslot')
        timeslot = TimeSlot.objects.get(id=timeslot_id)

        if timeslot.is_booked:
            return Response({"error": "Time slot already booked"}, status=status.HTTP_400_BAD_REQUEST)

        timeslot.is_booked = True
        timeslot.save()

        return super().create(request, *args, **kwargs)