from rest_framework import viewsets

from hotel_app.models import *
from hotel_app.serializers import *


# Create your views here.
class RoomAPIView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class EmployeeAPIView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class ResidentAPIView(viewsets.ModelViewSet):
    serializer_class = ResidentSerializer
    queryset = Resident.objects.all()


class BookingRecordAPIView(viewsets.ModelViewSet):
    serializer_class = BookingRecordSerializer
    queryset = BookingRecord.objects.all()


class CleaningScheduleAPIView(viewsets.ModelViewSet):
    serializer_class = CleaningScheduleSerializer
    queryset = CleaningSchedule.objects.all()