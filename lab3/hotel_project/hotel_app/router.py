from hotel_app.views import RoomAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('rooms', RoomAPIView)