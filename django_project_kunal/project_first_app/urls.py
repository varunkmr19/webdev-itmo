from django.urls import path

from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.detail, name='detail'),
    path('owner/create', views.CarOwnerCreate.as_view(), name='create'),
    path('car/<int:car_id>', views.car_detail, name='car_detail'),
    path('car/create', views.AddCar.as_view(), name='add_car'),
    path('car/<int:pk>/update', views.UpdateCar.as_view(), name='update_car')
]
