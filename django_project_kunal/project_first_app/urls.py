from django.urls import path

from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.detail, name='detail'),
    path('owner/create', views.CarOwnerCreate.as_view(), name='create')
]
