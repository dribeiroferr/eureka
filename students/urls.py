from django.contrib import admin
from django.urls import path
from views import StudentViewSet

urlpatterns = [
    path('students/', StudentViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('students/<str:pk>', StudentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'remove'
    }))
]
