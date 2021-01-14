from rest_framework import viewsets

from hotel_app.models import Room
from hotel_app.serializers import RoomSerializer


# Create your views here.
class RoomAPIView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
